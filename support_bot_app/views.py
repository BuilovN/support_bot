import json, os
from .models import Message
from .forms import ReplyMessageForm
from django.db.models import Max
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.views.decorators.csrf import csrf_exempt
from support_bot_app.lib.bot.support_bot import SupportBot

@csrf_exempt
def bot(request):
    request_body = json.loads(request.body)
    try:
        message = SupportBot.parse_update_to_message_model(request_body)
        message.save()
    except KeyError as e:
        print("Invalid json request")
    return HttpResponse(status=200)


def index(request):
    messages = Message.objects.values('telegram_id', 'first_name', 'last_name', 'username')\
                   .annotate(last_date=Max('date'),)\
                   .order_by('-last_date')[:10]

    print(os.environ['APIKEY'])
    return render(request,
                  "index.html",
                  context={
                    'messages': messages,
                  })


def dialog(request, id):
    chat_id = id
    messages = Message.objects.filter(telegram_id__exact=chat_id).order_by('date')
    print(messages)
    return render(request,
                  "dialog.html",
                  context={
                      "messages": messages,
                      "chat_id": chat_id
                  })


def send_message(request, id):
    bot = SupportBot()
    form = ReplyMessageForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        bot.send_message(id, text)

    return HttpResponseRedirect(f"/dialog/{id}")