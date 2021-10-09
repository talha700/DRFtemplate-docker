from django.urls import path
from django.conf.urls import url
from apps.users import views
from rest_framework import routers

user_router = routers.SimpleRouter()
user_router.register(r'',views.ManageUsers)



urlpatterns = [
    path('change_password/', views.ChangePassword.as_view(), name='change_password'),
]

urlpatterns += user_router.urls