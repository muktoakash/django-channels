"""chat/apps.py"""
from django.apps import AppConfig


class ChatConfig(AppConfig):
    """ChatConfig"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
