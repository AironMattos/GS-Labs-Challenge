from django.urls import path
from .views import home, create_product, delete_product, update_product, login

urlpatterns = [
    path('', home, name='home'),
    path('create', create_product, name='create'),
    path('delete/<str:pk>', delete_product, name='delete'),
    path('update/<str:pk>', update_product, name='update'),
    path('accounts/signup', login, name='login')
]