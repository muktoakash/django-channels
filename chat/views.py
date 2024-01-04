"""chat/views.py"""
from django.shortcuts import render

# Create your views here.

def index(request):
    """homescreen for chat lobby"""
    return render(request, "chat/index.html")

def room(request, room_name):
    """chat room"""
    return render(request, "chat/room.html", {"room_name": room_name})
