from django.contrib import admin
from .models import Messages
# Register your models here.


class MessageText(admin.ModelAdmin):
    fields = ['name','message','time_sent','email_id']
    list_display = ['name','message','time_sent','email_id']

admin.site.register(Messages, MessageText)