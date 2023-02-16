from django.contrib import admin
from .models import Article, Comment



class CommentInline(admin.StackedInline):
    model = Comment
    # extra = 0 # Limiting the extra fields

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)