from django.urls import path
from .views import Login, logout_account, Register

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_account, name='logout'),
    path('signup/', Register.as_view(), name='signup')
]