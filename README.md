# A django app to count online users.

## Install:
- Clone repository
- python setup.py install

## Configuration:
- Put 'onlineuser' on installed apps in your settings.py
- Put 'onlineuser.middleware.OnlineUserMiddleware' in your MIDDLEWARE_CLASSES
- Set your online duration. LAST_ONLINE_DURATION in settings.py. The default is 60 sec.

## Use:
{% load onlineuser_tags %}
{% onlineinfos %}
