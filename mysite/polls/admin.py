from django.contrib import admin
from polls.models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "pub_date", "was_published_recently")
    fieldsets = [
        ("Question Information", {'fields': ["question_text"]}),
        ("Date Information", {'fields': ["pub_date"], 'classes': ["collapse"]})
    ]
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)