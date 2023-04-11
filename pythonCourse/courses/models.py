from django.db.models import (CASCADE, CharField, DateTimeField, ForeignKey,
                              Model, TextField, IntegerField)

from .utils.dateUtils import *


class Topic(Model):
    name = CharField(max_length=50)
    created_by = CharField(max_length=50)
    creation_date = DateTimeField(auto_now_add=True)
    last_update_user = CharField(max_length=50)
    last_update = DateTimeField()

    def __str__(self) -> str:
        return "{}".format(self.name)

    def creation_date_info(self):
        return creation_or_update_date_info(self.creation_date, None, self.created_by)

    def update_date_info(self):
        return creation_or_update_date_info(None, self.last_update, self.last_update_user)


class Content(Model):
    '''
        Content in a Topic
        Can be seen as a chapter
    '''
    topic = ForeignKey(Topic, on_delete=CASCADE)
    name = CharField(max_length=50)
    description = TextField()
    created_by = CharField(max_length=50)
    creation_date = DateTimeField(auto_now_add=True)
    last_update_user = CharField(max_length=50)
    last_update = DateTimeField()

    def __str__(self) -> str:
        return "{}".format(self.name)

    def creation_date_info(self):
        return creation_or_update_date_info(self.creation_date, None, self.created_by)

    def update_date_info(self):
        return creation_or_update_date_info(None, self.last_update, self.last_update_user)


class ContentType(Model):
    '''
        Type of a content part
        Can be text/code/...
    '''
    name = CharField(max_length=50)
    description = CharField(max_length=200)

    def __str__(self) -> str:
        return "{}".format(self.name)


class ContentPart(Model):
    '''
        ContentPart in a Content
        Can be seen as a section
            section_number reflects the order the content part is displayed
    '''
    content = ForeignKey(Content, on_delete=CASCADE)
    type = ForeignKey(ContentType, on_delete=CASCADE)
    section_number = IntegerField()
    title = CharField(max_length=150)
    text = TextField()
    created_by = CharField(max_length=50)
    creation_date = DateTimeField(auto_now_add=True)
    last_update_user = CharField(max_length=50)
    last_update = DateTimeField()

    def __str__(self) -> str:
        return "Content Part nº{}".format(self.section_number)

    def creation_date_info(self):
        return creation_or_update_date_info(self.creation_date, None, self.created_by)

    def update_date_info(self):
        return creation_or_update_date_info(None, self.last_update, self.last_update_user)
