from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from .models import Posts, Comments, Tagging
# Register your models here.


class PostText(admin.ModelAdmin):
	fields = ['post_head','post_text']
	list_display = ('post_head','post_created_on')
	formfield_overrides={
		models.CharField:{'widget':TextInput(attrs={'size':'20'})},
		models.TextField:{'widget':Textarea(attrs={'rows':'4','cols':'40'})},
	}


admin.site.register(Posts, PostText)
admin.site.register(Comments)
admin.site.register(Tagging)
