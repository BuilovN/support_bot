import json
from django.shortcuts import HttpResponse
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
