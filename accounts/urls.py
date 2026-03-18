from django.urls import path
from . import views

urlpatterns = [
    path('cards/', views.users_cards, name='users_cards'),
    path('register/', views.register_user, name='register_user'),
]