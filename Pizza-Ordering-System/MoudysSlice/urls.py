from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', views.index, name="index"),
   path('register', views.register, name="register"),
   path("login", views.login, name="login"),
   path('logout/', views.logout_view, name='logout'),
   path("index2", views.index2, name="index2"),
   path("order", views.order, name="order"),
   path("details", views.details, name="details"),
   path("completed_orders", views.completed_order, name="completed_order"),
]
