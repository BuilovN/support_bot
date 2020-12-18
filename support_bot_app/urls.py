from django.urls import path

from . import views

urlpatterns = [
    path("bot", views.bot, name="bot",),
    path("", views.index, name="index"),

    path("dialog/<id>", views.dialog, name="dialog"),
    path("dialog/<id>/send", views.send_message, name="dialog")
]
