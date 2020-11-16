from django.contrib import admin
from .models import Question, Choice
admin.site.site_header ="Alphatech Solutions "
admin.site.site_title = "Alphatech solutions Admin"
admin.site.index_title ="Welcome to Alphatech Solutions Admin"
# admin.site.register(Question)
# admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)