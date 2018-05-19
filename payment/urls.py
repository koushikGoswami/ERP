from payment import views
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path



urlpatterns = [
    path('all_payment/',views.PaymentReadView.as_view()),
    path('all_payment/<pk>/',views.PaymentReadDetailView.as_view()),
    path('payment/', views.PaymentMatser.as_view()),
    path('payment/<pk>/', views.PaymentMatserUpdate.as_view()),


]
