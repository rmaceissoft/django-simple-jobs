from django.contrib import admin

from simple_jobs.models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')

admin.site.register(Job, JobAdmin)