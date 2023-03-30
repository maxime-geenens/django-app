from django.forms import *
from .models import Topic, Content, ContentPart


class TopicForm(ModelForm):

    class Meta:
        model = Topic
        fields = ["name", "created_by",]
        labels = {
            "name": "Name",
            "created_by": "Created By",
        }


class ContentForm(ModelForm):

    class Meta:
        model = Content
        fields = ["name", "description", "topic",]
        labels = {
            "name": "Name",
            "topic": "Topic",
            "description": "Description",
        }
        widgets = {"description": Textarea(attrs={'rows': 2})}


class ContentListForm(ModelForm):
    class Meta:
        model = Content
        fields = ["topic",]
        labels = {
            "topic": "Topic",
        }
        widgets = {'topic': Select(attrs={'onChange': 'submit();'})}


class ContentPartForm(ModelForm):

    class Meta:
        model = ContentPart
        fields = ["title", "type", "section_number", "text"]
        labels = {
            "title": "Title",
            "type": "Type",
            "section_number": "Order",
            "text": "Content",
        }
