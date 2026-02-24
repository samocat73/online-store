from django.contrib import admin

from blog.models import Article


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ("id", "title", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "content")
