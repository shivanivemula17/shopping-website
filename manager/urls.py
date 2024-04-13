from django.urls import path
from . import views
urlpatterns=[
    path('',views.manager,name='manager'),
    path('manager_profile/',views.manager_profile,name='manager_profile'),
    path('add_item/',views.add_item,name='add_item'),
    path('customer_list/',views.customer_list,name='customer_list'),
    path('feedbacks/',views.feedbacks,name='feedbacks'),
    path('historys/',views.historys,name='historys'),
    path('Item_List/',views.Item_List,name='Item_List'),
]