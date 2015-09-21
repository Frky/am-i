from django.conf.urls import include, url

import website.views

urlpatterns = [
    url(r'^$', view=website.views.index, name="index"),
    url(r'^ping$', view=website.views.ping, name="ping"),
]
