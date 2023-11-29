from django.contrib import admin
from .models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin

# customize adim panel

class Postadmin(SummernoteModelAdmin):
    list_display=['title','draft']
    list_filter=['title','tags']
    search_fields=['title','draft']
class Commentadmin(admin.ModelAdmin):
    list_display=['post','author']
    list_filter=['publish_date']
    search_fields=['post']



# Register your models here.
admin.site.register(Post,Postadmin)
admin.site.register(Category)
admin.site.register(Comment)

