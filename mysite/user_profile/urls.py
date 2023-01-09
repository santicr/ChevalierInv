from django.urls import path
from .views import login_req, logout_req

urlpatterns = [
    path('login/', login_req, name = 'login_req'),
    path('logout/', logout_req, name = 'logout_req'),
]
