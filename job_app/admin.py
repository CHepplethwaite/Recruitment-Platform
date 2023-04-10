from django.contrib import admin
from .models import job

class jobAdmin(admin.ModelAdmin):
    list_display=('job_title',"company","post_date","closing_date","status","user")
    prepopulated_fields={"slug":("job_title",)}

admin.site.register(job,jobAdmin)
