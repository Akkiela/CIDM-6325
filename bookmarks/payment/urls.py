from django.urls import path,include

from . import views
from django.contrib import admin


app_name = 'payment'

urlpatterns = [
    path('process/', views.payment_process, name='process'),
    path('completed/', views.payment_completed, name='completed'),
    path('canceled/', views.payment_canceled, name='canceled'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('cancel/', views.cancel, name='cancel'),
    path('success/', views.success, name='success'),
    path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
    path('direct-to-customer-portal/', views.direct_to_customer_portal, name='direct-to-customer-portal'),
    path('collect-stripe-webhook/', views.collect_stripe_webhook, name='collect-stripe-webhook'),
]

   
