from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('module_admin/',views.module_admin,name='module_admin'),
    path('module_manager/',views.module_manager,name='module_manager'),
    path('module_user/',views.module_user,name='module_user'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup')
]