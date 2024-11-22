from django.contrib import admin
from .models import Task, OAuthKey

admin.site.register(Task)
admin.site.register(OAuthKey)
