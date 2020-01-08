from django.contrib import admin
from django.urls import path, include
from accounts.views import req_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('movies/', include('movies.urls')),
    path('recommend/', include('recommend.urls')),
    path('', req_login),
]
