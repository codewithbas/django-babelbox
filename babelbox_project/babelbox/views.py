import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from .models import Message
from .forms import MessageForm



def index(request):
    messages = Message.objects.all()
    languages = settings.TRANSLATED_LANGUAGES
    return render(request, 'babelbox/index.html', dict(messages=messages, languages=languages))


def add(request):
    form = MessageForm(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(request, 'babelbox/add.html', dict(form=form))