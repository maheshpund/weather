from django.urls import path, re_path

from . import views

urlpatterns = [
    path('',views.UserView),
    path('l/',views.login,name='login'),
    path('w/',views.Weather.as_view(),name='weather'),
]