from django.contrib import admin
from .models import *


# Register your models here.

class GalleryInline(admin.TabularInline):
    fk_name = 'news'
    model = NewsImage
    extra = 3


class DescInline(admin.TabularInline):
    fk_name = 'news'
    model = NewsDesc
    extra = 3


admin.site.register(Gender)
admin.site.register(Region)
admin.site.register(Faculty)
admin.site.register(StudyType)
admin.site.register(ExamLang)
admin.site.register(Document)

admin.site.register(NewsCategory)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'status')
    list_display_links = ('title',)
    list_editable = ('status',)
    list_filter = ('created_at', 'category')
    inlines = [GalleryInline, DescInline]

admin.site.register(Article)
admin.site.register(SliderPhoto)
