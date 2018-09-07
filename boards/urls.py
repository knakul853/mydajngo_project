from django.urls import path
from . import views

urlpatterns = [
    path('boards/<int:pk>/',views.board_topics,name='board_topics'),
    path('',views.home,name='home'),



]