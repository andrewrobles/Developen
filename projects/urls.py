from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('create-account/', views.create_account, name='create_account'),
    path('delete-account/', views.delete_account, name='delete_account')
]
