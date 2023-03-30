from django.urls import path

from .views import *

app_name = 'courses'
urlpatterns = [
    path('home/', home, name='home'),
    path('topic/<int:pk>/', topic, name='topic'),
    path('topic/<int:topic_id>/content/<int:pk>/', content, name='content'),
    path('create/', create, name='create'),
    path('createTopic/', createTopic, name='createTopic'),
    path('createContent/', createContent, name='createContent'),
    path('createContentPart/', createContentPart, name='createContentPart'),
]
