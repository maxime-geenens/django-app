from django.shortcuts import render
from django.http import Http404

from .models import *


def home(request):
    topic_list = Topic.objects.all()
    context = {
        'topic_list': topic_list,
    }
    return render(request, 'courses/home.html', context)


def topic(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
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
        content_lines = []
        for content_part in content_part_list:
            lines = ContentLine.objects.filter(content_part=content_part)
            p_lines = []
            for line in lines:
                p_lines.append(line)
            content_lines.append(p_lines)
    except Content.DoesNotExist:
        raise Http404("Content doesn't exists")
    context = {
        'content_part_list': content_part_list,
        'content': content,
        'content_lines': content_lines,
    }
    return render(request, 'courses/content.html', context)


def create(request):
    return render(request, 'courses/create.html')


def createTopic(request):
    return render(request, 'courses/createTopic.html')


def createContent(request):
    return render(request, 'courses/createContent.html')
