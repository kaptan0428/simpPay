from django.urls import path,include
from . import views # it import views

urlpatterns = [
                path('loogin',views.loogin,name='loogin'),

        path('',views.handleSignup,name='home'),
        path('pay',views.pay,name='pay'),
        path('logout',views.handle_logout,name='logout')
]