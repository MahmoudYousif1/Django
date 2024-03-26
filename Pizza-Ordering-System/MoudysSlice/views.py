from telnetlib import LOGOUT
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.core.exceptions import ValidationError
from datetime import datetime
from .forms import PizzaOrderForm
from .forms import DeliveryForm
from django.contrib.auth.decorators import login_required
from .models import Pizza
from .forms import *

def index(request):
    return render(request, "index.html")

@login_required
def index2(request):
    user_orders = request.user.orders.all().order_by('-order_time')
    return render(request, "index2.html", {'orders': user_orders})



def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = authenticate(
            request, user=request.POST["user"], password=request.POST["password"]
        )
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Login successful")
            return redirect("index2")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("index")
    

def order(request):
    if request.method == "POST":
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            order_instance = form.save()
            request.session["order_id"] = order_instance.id
            return redirect("details")
    else:
        form = PizzaOrderForm()

    return render(request, "order.html", {"form": form})


@login_required
def details(request):
    if request.method == "POST":
        form = DeliveryForm(request.POST)
        if form.is_valid():
            try:
                order_id = request.session.get("order_id")
                if order_id is None:
                    raise Pizza.DoesNotExist

                pizza_order = Pizza.objects.get(id=order_id)
                pizza_order.user = request.user
                pizza_order.save()
                
                delivery_info = form.save(commit=False)
                delivery_info.pizza = pizza_order
                delivery_info.save()

                del request.session["order_id"]

                messages.success(request, "Your order has been completed successfully.")
                return redirect("completed_order")
            except Pizza.DoesNotExist:
                messages.error(
                    request, "Order not found. Please start your order again."
                )
                return redirect("order")
    else:
        form = DeliveryForm()

    return render(request, "details.html", {"form": form})


@login_required
def completed_order(request):
    try:
        user_order = request.user.orders.order_by('-order_time').first()
        if user_order:
            delivery_info = user_order.delivery.first()
            if delivery_info:
                context = {'order': user_order, 'delivery': delivery_info}
            else:
                messages.error(request, "Delivery information could not be found for this order.")
                context = {'order': user_order}
        else:
            messages.error(request, "No recent order found.")
            return redirect('order')
    except Pizza.DoesNotExist:
        messages.error(request, "Order not found.")
        return redirect('order')

    return render(request, "completed_order.html", context)
