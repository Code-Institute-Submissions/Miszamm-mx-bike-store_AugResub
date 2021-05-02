from django.contrib import admin
from django.urls import path
from .views import (
    CheckoutView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    PaymentView,
    remove_single_item_from_cart,
    create_checkout_session
)


urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session')
]