from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'body', 'created_on')
    orderinig = ('-created_on')


admin.site.register(Contact)