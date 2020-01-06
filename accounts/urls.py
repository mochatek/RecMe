from django.urls import path, include 
from . import views

app_name="accounts"

urlpatterns=[
    # auth will supply login -> accounts/login
    path('login/', views.req_login, name = "login"),
    path('signup/', views.req_signup, name = "signup"),
    path('logout/', views.req_logout, name = "logout"),
]