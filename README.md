# django-channels
Implement a basic chatting app using django channels. Following [medium article](https://medium.com/atomic-loops/django-channels-is-all-you-need-94628dd6815c). This, or a very similar example, can also be found on the official [documentation for Channels](https://channels.readthedocs.io/en/latest/tutorial/index.html).

## The end result

Two browser windows entering the same chat room from lobby.
![Two browser windows entering the same chat room from lobby.](image.png)
One window saying "Hi" to  the other.
![One window sending a message to another](image-1.png)
Second window replying to the "Hi" message.
![One window replying to a message from the other](image-2.png)
Both windows can see all messages sent and received.
![Both windows showing the messages](image-3.png)
Not that this has not implemented user authentication, so the chat messages do not show who sent which message.

## Packages:
All installed packages are listed in [requirements.txt](./requirements.txt)

## New Terms that I learned:
### Channels and consumers
[Channels](https://channels.readthedocs.io/en/latest/) is a project that takes Django and extends its abilities beyond HTTP - to handle WebSockets, chat protocols, IoT protocols, and more. It’s built on a Python specification called ASGI.

This project uses the following packages for Channels:
- Channels, the Django integration layer
- Daphne, the HTTP and Websocket termination server
- asgiref, the base ASGI library
- channels_redis, the Redis channel layer backend (used with docker)

Channels uses something called consumers (the equivalent of Django views). These consumers are like friendly assistants that know how to handle different types of real-time communication events, such as receiving a new message in the chat. Unlike Django views, consumers are long-running. 

Channels gives us the tools to write these basic consumers - individual pieces that might handle chat messaging, or notifications - and tie them together with URL routing, protocol detection and other handy things to make a full application.

Test the implementation of the channel layers with the following shell commmands:
```$ python3 manage.py shell
import channels.layers
channel_layer = channels.layers.get_channel_layer()
from asgiref.sync import async_to_sync
async_to_sync(channel_layer.send)('test_channel', {'type': 'hello'})
async_to_sync(channel_layer.receive)('test_channel')
```
### Daphne
    `python -m pip install -U 'channels[daphne]'`
Daphne is a HTTP and WebSockets protocol server for ASGI to power Django-Channels.

## Views:
- (Chat Room lobby)[./chat/templates/chat/index.html]

## Files:
All relevant files can be found in [files.txt](./files.txt)