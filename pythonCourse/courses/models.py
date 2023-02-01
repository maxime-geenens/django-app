from django.db.models import (CASCADE, CharField, DateTimeField, ForeignKey,
                              Model, TextField, IntegerField)

from .utils.dateUtils import when_was_created


class Topic(Model):
    name = CharField(max_length=50)
    creation_date = DateTimeField('date created')
    created_by = CharField(max_length=50)

    def __str__(self) -> str:
        return "{} created by: {} on: {}".format(self.name, self.created_by, self.creation_date)

    def created_recently(self):
        return when_was_created(self.creation_date)


class Content(Model):
    topic = ForeignKey(Topic, on_delete=CASCADE)
    name = CharField(max_length=50)
    description = TextField()

    def __str__(self) -> str:
        return "Content: {} || Belongs to Topic: {}".format(self.name, self.topic.name)


class ContentPart(Model):
    content = ForeignKey(Content, on_delete=CASCADE)
    order = IntegerField(unique=True)
    title = CharField(max_length=50)
    text = TextField()

    def __str__(self) -> str:
        return "ContentPart nº{}: {} || Belongs to Content: {}".format(self.order, self.title, self.content.name)


class LineType(Model):
    name = CharField(max_length=50)
    description = CharField(max_length=200)

    def __str__(self) -> str:
        return "Line Type: {}".format(self.name)


class ContentLine(Model):
    type = ForeignKey(LineType, on_delete=CASCADE)
    content_part = ForeignKey(ContentPart, on_delete=CASCADE)
    order = IntegerField(unique=True)
    text = TextField()#try to save some text from sql

    def __str__(self) -> str:
        return "ContentLine nº{} of ContentPart: {}".format(self.order, self.content_part.title)
