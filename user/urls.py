from django.urls import path
from . import views
urlpatterns=[path('',views.user,name='user'),
             path('user_profile/',views.user_profile,name='user_profile'),
             path('cart/',views.cart,name='cart'),
             path('feedback/',views.feedback,name='feedback'),
             path('history/',views.history,name='history'),
             path('items_list/',views.items_list,name='items_list'),
             path('order_display/',views.order_display,name='order_display'),
             path('tracking/',views.tracking,name='tracking')]