from django.shortcuts import render
from django.http import Http404

from .models import *
from .forms import *


def home(request):
    topic_list = Topic.objects.all()
    context = {
        'topic_list': topic_list,
    }
    return render(request, 'courses/home.html', context)


def topic(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
        content_list = Content.objects.filter(topic=topic)
    except Topic.DoesNotExist:
        raise Http404("Topic doesn't exists")
    context = {
        'content_list': content_list,
        'topic': topic
    }
    return render(request, 'courses/topic.html', context)


def content(request, topic_id, content_id):
    try:
        content = Content.objects.get(pk=content_id)
        content_part_list = ContentPart.objects.filter(content=content)

    except Content.DoesNotExist:
        raise Http404("Content doesn't exists")
    context = {
        'content': content,
        'content_parts': content_part_list,
    }
    return render(request, 'courses/content.html', context)


def create(request):
    return render(request, 'courses/create.html')


def createTopic(request):
    topic_list = Topic.objects.all()
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TopicForm()
    
    context = {
        'form': form,
        'topic_list': topic_list,
    }

    return render(request, 'courses/createTopic.html', context)


def createContent(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContentForm()

    return render(request, 'courses/createContent.html', {'form': form})
