from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Topic, Content, ContentPart, LineType, ContentLine])