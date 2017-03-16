# A django app to count online users.

## Install:
- Clone repository
- python setup.py install

## Configuration:
- Put 'onlineuser' on installed apps in your settings.py
- Put 'onlineuser.middleware.OnlineUserMiddleware' in your MIDDLEWARE_CLASSES
- Set a url: url(r'^online-users/$', onlineusers.views.get_online_users, name='online_users'),
- Set your online duration. LAST_ONLINE_DURATION in settings.py. The default is 60 sec.

## Use:
### Template tags:
{% load onlineuser_tags %}
{% onlineinfos %}

### Json:
- Call your url.
