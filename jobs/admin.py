from django.contrib import admin

# Register your models here.
from .models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ['summary', 'image']


admin.site.register(Job, JobAdmin)
