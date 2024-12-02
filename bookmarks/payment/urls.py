from django.urls import path,include

from . import views
from .views import cancel_view,checkout_view,success_view
from django.contrib import admin


app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('checkout/<int:plan_id>/', views.checkout_view, name='checkout'),
    path('cancel/', views.cancel_view, name='cancel'),
    path('success/', views.success_view, name='success'),
]

   
