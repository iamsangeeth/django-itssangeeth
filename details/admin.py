from django.contrib import admin
from .models import Messages
# Register your models here.


class MessageText(admin.ModelAdmin):
    fields = ['name','message','time_sent']
    list_display = ['name','message','time_sent']

admin.site.register(Messages, MessageText)