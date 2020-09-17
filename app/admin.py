from django.contrib import admin
from app.models import *
# Register your models here.

class WebpageAdminView(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_editable=('url',)
    list_display_links=['name']
    list_per_page=2
    search_fields=['name']
    list_filter=['topic_name','name','url']





admin.site.register(Topic)
admin.site.register(Webpage,WebpageAdminView)
admin.site.register(Access_Records)