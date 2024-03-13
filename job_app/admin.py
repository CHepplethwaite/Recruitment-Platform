from django.contrib import admin
from .models import job

class jobAdmin(admin.ModelAdmin):
    list_display=("status","details","user",'country','job_title',"employment_type","industry","post_date","closing_date","logo",)

admin.site.register(job,jobAdmin)
