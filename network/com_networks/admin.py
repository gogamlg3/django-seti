from django.contrib import admin
from .models import Topic, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'topic')
    list_filter = ('topic',)
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('is_correct',)
