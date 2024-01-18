from django.contrib import admin
from .models import job

class jobAdmin(admin.ModelAdmin):
    list_display=("details","user",'job_title',"slug","employment_type","industry","post_date","closing_date","logo","status")
    prepopulated_fields={"slug":("job_title",)}

admin.site.register(job,jobAdmin)
