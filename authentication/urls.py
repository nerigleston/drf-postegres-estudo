from django.urls import path
from .views import (
    login,
    logout,
    signup,
    test_token
)

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('test_token/', test_token, name='test_token'),
    path('logout/', logout, name='logout'),
]
