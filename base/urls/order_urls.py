from django.urls import path
from base.views import order_views as views

urlpatterns = [
    # for owner and employee
    path('restaurant_orders/', views.getResOrders, name='restaurant-orders'),
    path('myorders/', views.getMyOrders, name='myorders'),

    # for user
    path('add/', views.addOrderItems, name='orders-add'),
    path('<str:pk>/', views.getOrderById, name='user-order'),
    path('make_payment/<str:pk>/', views.makePayment, name='payment'),
]