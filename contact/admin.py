from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'body', 'created_on', 'complete')
    list_editable = ('complete',)
    ordering = ('-created_on',)


admin.site.register(Contact, ContactAdmin)