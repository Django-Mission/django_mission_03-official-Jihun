from django.contrib import admin

from .models import Post, Comment

# Register your models here.

# class CommentInline(admin.TabularInline):
#     model = Comment



# @admin.register(Post)
# class PostModelAdmin(admin.ModelAdmin):
#     list_display = ('id', 'image', 'content', 'created_at',  'view_count',  'writer')
#     # list_editable = ('content',)
#     list_filter = ('created_at',)
    
#     search_fields = ('id',)
#     search_help_text = '계시판 번호, 작성자 검색이 가능합니다'

#     inlines = [CommentInline]


# admin.site.register(Comment)
