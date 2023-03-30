from django.shortcuts import render
from django.http import Http404

from .models import *
from .forms import *
from .utils.dictUtils import *

base_context: dict = {
    'topic_list': Topic.objects.all(),
}


def home(request):
    return render(request, 'courses/home.html', base_context)


def navbar(request):
    return render(request, 'courses/navbar.html', base_context)


def topic(request, pk):
    try:
        topic = Topic.objects.get(pk=pk)
        content_list = Content.objects.filter(topic=topic)
    except Topic.DoesNotExist:
        raise Http404("Topic doesn't exists")
    context: dict = {
        'content_list': content_list,
        'topic': topic,
    }
    return render(request, 'courses/topic.html',  merge(base_context, context))


def content(request, topic_id, pk):
    try:
        content = Content.objects.get(pk=pk)
        content_part_list = ContentPart.objects.filter(content=content)
        topic = Topic.objects.get(pk=topic_id)
        content_list = Content.objects.filter(topic=topic)
    except Content.DoesNotExist:
        raise Http404("Content doesn't exists")
    context = {
        'content': content,
        'content_list': content_list,
        'content_parts': content_part_list,
    }
    return render(request, 'courses/content.html', merge(base_context, context))


def create(request):
    return render(request, 'courses/create.html', base_context)


def createTopic(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TopicForm()

    context = {
        'form': form,
    }

    return render(request, 'courses/createTopic.html', merge(base_context, context))


def createContent(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContentForm()

    content_list = []

    if request.method == "GET":
        form2 = ContentListForm(request.GET)
        selected_topic = request.GET.get("topic")
        content_list = Content.objects.all().filter(topic=selected_topic)
    else:
        form2 = ContentListForm()

    context = {
        'form': form,
        'form2': form2,
        'content_list': content_list
    }

    return render(request, 'courses/createContent.html', merge(base_context, context))


def createContentPart(request):
    pass
