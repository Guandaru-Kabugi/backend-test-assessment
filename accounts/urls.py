from django.urls import path
from .views import CreateNewAdminUser,login_view

urlpatterns = [
    path('create-admin/', CreateNewAdminUser.as_view(), name='create-admin-user'),
    path('login/', login_view, name='login-view'),
]