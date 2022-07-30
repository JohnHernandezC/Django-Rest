from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from userApp.api.views import registration_view,logout_view

urlpatterns=[
    path('login/', obtain_auth_token, name='login'),
    path('register/', registration_view, name='registrar'),
    path('logout/', logout_view, name='logout'),
]