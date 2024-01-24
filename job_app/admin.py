from django.contrib import admin
from .models import job

class jobAdmin(admin.ModelAdmin):
    list_display=("details","user",'job_title',"employment_type","industry","post_date","closing_date","logo","status")
    list_filter=("status","post_date","closing_date")
    search_fields=("details","user",'job_title',"employment_type","industry","post_date","closing_date","logo","status")

admin.site.register(job,jobAdmin)
