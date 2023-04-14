from django.urls import path

from .views import *

app_name = 'courses'
urlpatterns = [
    path('home/', home, name='home'),
    path('topic/<int:pk>/', topic, name='topic'),
    path('topic/<int:pk>/update/', topicUpdate, name='topicUpdate'),
    path('topic/<int:topic_id>/content/<int:pk>/', content, name='content'),
    path('topic/<int:topic_id>/content/<int:pk>/update/', contentUpdate, name='contentUpdate'),
    path('topic/<int:topic_id>/content/<int:content_id>/contentPart/<int:pk>/update/', contentPartUpdate, name='contentPartUpdate'),
    path('create/', create, name='create'),
    path('createTopic/', createTopic, name='createTopic'),
    path('createContent/', createContent, name='createContent'),
    path('createContentPart/', createContentPart, name='createContentPart'),
]
