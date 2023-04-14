from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user

from .models import *
from .forms import *
from .utils.dictUtils import *

base_context: dict = {
    'topic_list': Topic.objects.all(),
}

# Basic screens


@login_required
def home(request):
    return render(request, 'courses/home.html', base_context)


def navbar(request):
    return render(request, 'courses/navbar.html', base_context)


@login_required
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


@login_required
def content(request, topic_id, pk):
    try:
        content = Content.objects.get(pk=pk)
        content_part_list = ContentPart.objects.filter(
            content=content).order_by('section_number')
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

# Create screens


@login_required
def create(request):
    context: dict = {
    }
    return render(request, 'courses/create.html', merge(base_context, context))


@login_required
def createTopic(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        username = get_user(request).get_username()
        form = TopicForm(initial={'created_by': username})

    context = {
        'form': form,
    }

    return render(request, 'courses/createTopic.html', merge(base_context, context))


@login_required
def createContent(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        username = get_user(request).get_username()
        form = ContentForm(initial={'created_by': username})

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
        'content_list': content_list,
    }

    return render(request, 'courses/createContent.html', merge(base_context, context))


@login_required
def createContentPart(request):
    cp = ContentPart()
    if request.method == "POST":
        form = ContentPartForm(request.POST, instance=cp)
        if form.is_valid():
            content_parts = ContentPart.objects.all().filter(
                content=form.data["content"])
            order = len(content_parts) + 1
            new_part = form.save(commit=False)
            new_part.section_number = order
            new_part.save()
            form.save_m2m()
    else:
        username = get_user(request).get_username()
        form = ContentPartForm(initial={'created_by': username})

    content_part_list = []

    if request.method == "GET":
        form2 = ContentPartListForm(request.GET)
        selected_content = request.GET.get("content")
        content_part_list = ContentPart.objects.all().filter(content=selected_content)
    else:
        form2 = ContentListForm()

    context = {
        'form': form,
        'form2': form2,
        'content_part_list': content_part_list,
    }

    return render(request, 'courses/createContentPart.html', merge(base_context, context))


# Update screens
def topicUpdate(request, pk):

    topic = Topic.objects.get(id=pk)

    if request.method == "POST":
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
    else:
        username = get_user(request).get_username()
        form = TopicForm(
            initial={
                'last_update_user': username,
                'last_update': timezone.now
            },
            instance=topic
        )

    context = {
        'form': form,
        'topic': topic,
    }

    return render(request, "courses/updateTopic.html", merge(base_context, context))


def contentUpdate(request, id):
    pass


def contentPartUpdate(request, id):
    pass
