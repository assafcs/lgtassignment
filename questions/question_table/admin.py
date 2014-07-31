from django.contrib import admin
from question_table.models import Question

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("The Question's title", {'fields': ['title']}),
        ("The Question itself", {
            'fields': ['description'], 'classes': ['collapse']})
        ]
    list_display = ('title', 'description')

admin.site.register(Question, QuestionAdmin)
