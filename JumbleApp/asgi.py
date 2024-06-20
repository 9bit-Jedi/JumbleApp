"""
ASGI config for JumbleApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter , URLRouter
from messaging import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JumbleApp.settings')

application  = get_asgi_application()

application = ProtocolTypeRouter({
    "http": application,
    # Add WebSocket routing here later (e.g., 'websocket': AuthMiddlewareStack(URLRouter(...)))
    "websocket" : AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )    
        )
})
