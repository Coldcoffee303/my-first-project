

from . import views
from django.urls import path


urlpatterns = [
	path('', views.home,name='Home'),
	path('chatroom/<str:pk>',views.chatroom, name='chat-room'),
	path('createroom',views.createRoom,name='create-room'),
	path('updateroom<str:pk>',views.updateRoom,name='update-room'),
	path('deleteroom<str:pk>',views.deleteRoom, name='delete-room'),
]

