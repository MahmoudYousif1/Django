from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *
from .models import OrderDelivery
from .models import Pizza

User = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs.update({'class': 'form-control'})
        for fieldname in ['password1', 'password2']:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('user', 'email')


class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))



class PizzaOrderForm(forms.ModelForm):
    size = forms.ModelChoiceField(queryset=Size.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    crust = forms.ModelChoiceField(queryset=Crust.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    sauce = forms.ModelChoiceField(queryset=Sauce.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    cheese = forms.ModelChoiceField(queryset=Cheese.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    Pepperoni = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    Chicken = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    Ham = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    Pineapple = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    Peppers = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    Mushrooms = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    Onions = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    Sausages = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    Jalapeños = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    Pesto = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    
    class Meta:
        model = Pizza
        fields = [
            "size",
            "crust",
            "sauce",
            "cheese",
            "Pepperoni",
            "Chicken",
            "Ham",
            "Pineapple",
            "Peppers",
            "Mushrooms",
            "Onions",
            "Sausages",
            "Jalapeños",
            "Pesto",
        ]



class DeliveryForm(forms.ModelForm):
    class Meta:
        model = OrderDelivery
        fields = ["name", "address", "card", "expirydate", "cvv"]
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            "address": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'}),
            "card": forms.NumberInput(attrs={"class": "form-control", "type": "text", "maxlength": "16"}),
            "expirydate": forms.TextInput(attrs={"class": "form-control", "placeholder": "MM/YY"}),
            "cvv": forms.NumberInput(attrs={"class": "form-control", "type": "text", "maxlength": "3"}),
        }