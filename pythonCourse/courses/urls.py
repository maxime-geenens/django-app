from django.urls import path

from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('topic/<int:topic_id>/', topic, name='topic'),
    path('topic/<int:topic_id>/content/<int:content_id>/', content, name='content'),
    path('create/', create, name='create'),
    path('createContent/', createContent, name='createContent'),
    path('createTopic/', createTopic, name='createTopic'),
]
