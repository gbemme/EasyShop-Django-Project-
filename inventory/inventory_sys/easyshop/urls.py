from . import views
from django.urls import path

urlpatterns = [
    path('',views.show_product,name='show_product'),
    path('product/<int:pk>/',views.buy_product,name='buy_product'),
    path('product/payment',views.make_payment,name='make_payment'),
    path('product/message',views.message,name='message'),
]