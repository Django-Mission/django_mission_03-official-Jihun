from django.contrib import admin

from .models import Faq, Inquiry, Answer

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'modifed_at')
    list_filter = ('category',)
    
    search_fields = ('content',)
    search_help_text = '제목으로 검색이 가능합니다.'

    def save_model(self, request, obj, form, change):
        if not obj.writer:
            obj.writer = request.user
        obj.last_modifier = request.user
        obj.save()


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'writer', 'created_at')
    list_filter = ('category','state')
    
    search_fields = ('title', 'writer', 'e_mail','phone_number')
    search_help_text = '제목/작성자/이메일/전화번호로 검색이 가능합니다.'

    def save_model(self, request, obj, form, change):
        if not obj.writer:
            obj.writer = request.user
        obj.last_modifier = request.user
        obj.save()

        if obj.state == 'Finish':
            print(f"email : {obj.e_mail}\nphone : {obj.phone_number}")

    inlines = [AnswerInline]


