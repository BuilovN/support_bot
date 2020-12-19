import json, os
from math import ceil
from .lib.paginator.custom_paginator import CustomPaginator
from .lib.db.sql_templates import *
from .models import Message, Customer
from .forms import ReplyMessageForm
from datetime import datetime as dt
from django.db.models import Max
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from support_bot_app.lib.bot.support_bot import SupportBot
from datetime import datetime as dt

@csrf_exempt
def bot(request):
    request_body = json.loads(request.body)
    try:
        message = SupportBot.parse_update_to_message_model(request_body)
        try:
            message.full_clean()
            message.save()
        except ValidationError as e:
            print(e)
        customer = SupportBot.parse_update_to_customer_model(request_body)
        try:
            Customer.objects.get(telegram_id=customer.telegram_id)
        except Customer.DoesNotExist:
            try:
                customer.full_clean()
                customer.save()
            except ValidationError as e:
                print(e)
    except KeyError as e:
        return HttpResponse("Invalid arguments", status=400)
    return HttpResponse(status=200)


def index(request):
    dialogs_count = Customer.objects.count()
    dialogs_per_page = 10
    pages_count = ceil(dialogs_count / dialogs_per_page)
    pagination_range = 2
    page = request.GET.get('page')
    try:
        page = int(page)
        if page > pages_count:
            page = pages_count
        if page <= 0:
            raise ValueError
    except (TypeError, ValueError) as e:
        page = 1

    paginator = CustomPaginator(pages_count, pagination_range)
    pagination_list = paginator.pagination_list(page)
    messages = Message.objects.raw(get_joined_consumers_to_messages_last_message())[(page - 1) * 10 : page * 10]
    return render(request,
                  "index.html",
                  context={
                    'messages': messages,
                    'pagination_list': pagination_list,
                    'pages_count': pages_count,
                    'page': page,
                  })


def dialog(request, id):
    chat_id = id
    messages = Message.objects.filter(telegram_id__exact=chat_id).order_by('date')
    for message in messages:
        if not message.checked:
            message.checked = True
            message.save()
    try:
        username = Customer.objects.get(telegram_id=chat_id).username
    except Customer.DoesNotExist:
        return page_404(request)

    return render(request,
                  "dialog.html",
                  context={
                      "messages": messages,
                      "chat_id": chat_id,
                      "username": username
                  })


def send_message(request, id):
    bot = SupportBot()
    if Customer.objects.filter(telegram_id=id).exists():
        form = ReplyMessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            bot.send_message(id, text)
            message = Message(text=text,
                              telegram_id=id,
                              date=dt.now().replace(microsecond=0),
                              is_reply=True,
                              checked=True)
            try:
                message.full_clean()
                message.save()
            except ValidationError as e:
                print(e)
            return HttpResponseRedirect(f"/dialog/{id}")
    return page_404(request)


def page_404(request):
    return render(request,
                  '404.html')
