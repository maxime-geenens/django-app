from django.forms import *
from .models import Topic, Content, ContentPart


class TopicForm(ModelForm):

    class Meta:
        model = Topic
        fields = ["name", "created_by", "last_update_user", "last_update",]
        labels = {
            "name": "Name",
            "created_by": "Created By",
        }
        widgets = {
            "created_by": HiddenInput(),
            "last_update_user": HiddenInput(),
            "last_update": HiddenInput(),
        }


class ContentForm(ModelForm):

    class Meta:
        model = Content
        fields = ["name", "description", "topic", "created_by",]
        labels = {
            "name": "Name",
            "topic": "Topic",
            "description": "Description",
            "created_by": "Created By",
        }
        widgets = {
            "description": Textarea(attrs={'rows': 2}),
            'created_by': HiddenInput()
        }


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
        fields = ["title", "content", "type", "text", "created_by"]
        labels = {
            "title": "Title",
            "content": "Content",
            "type": "Type",
            "text": "Content",
            "created_by": "Created By",
        }
        widgets = {
            "text": Textarea(attrs={'rows': 2}),
            "created_by": HiddenInput(),
        }


class ContentPartListForm(ModelForm):
    class Meta:
        model = ContentPart
        fields = ["content",]
        labels = {
            "content": "Content",
        }
        widgets = {'content': Select(attrs={'onChange': 'submit();'})}
