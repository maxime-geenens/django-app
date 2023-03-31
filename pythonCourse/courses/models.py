from django.db.models import (CASCADE, CharField, DateTimeField, ForeignKey,
                              Model, TextField, IntegerField)

from .utils.dateUtils import when_was_created


class Topic(Model):
    name = CharField(max_length=50)
    creation_date = DateTimeField(auto_now_add=True)
    created_by = CharField(max_length=50)

    def __str__(self) -> str:
        return "{}".format(self.name)

    def created_recently(self):
        return when_was_created(self.creation_date)


class Content(Model):
    '''
        Content in a Topic
        Can be seen as a chapter
    '''
    topic = ForeignKey(Topic, on_delete=CASCADE)
    name = CharField(max_length=50)
    description = TextField()

    def __str__(self) -> str:
        return "{}".format(self.name)


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

    def __str__(self) -> str:
        return "Content Part nº{}".format(self.section_number)
