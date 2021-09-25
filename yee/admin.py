from yee.models import Letter
from django.contrib import admin

# Register your models here.

class LettersAdmin(admin.ModelAdmin):
    list_display = ('text', 'email', 'address', 'messages')

admin.site.register(Letter, LettersAdmin)