from django.contrib import admin
from .models import Invitation,OAuthSettings,Task

# Register your models here.

admin.site.register(Invitation)
admin.site.register(OAuthSettings)
admin.site.register(Task)

