from django.contrib import admin

# Register your models here.
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,{"fields":["question_text"]}),("Date Information",{"fields":["publication_date"],"classes":["collapse"]}),
    ]
    inlines=[ChoiceInline]
    list_display = ["question_text", "publication_date"]

admin.site.register(Question,QuestionAdmin)
