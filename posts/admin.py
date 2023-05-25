from django.contrib import admin
from django.contrib.admin import AdminSite
from job_app.models import job

class UserJobAdminSite(AdminSite):
    site_header = 'Manage jobs'  # Customize the header text
    site_title = 'Manage jobs'   # Customize the browser tab title

tumpe_admin_site = UserJobAdminSite(name='manage-jobs')

tumpe_admin_site.register(job)

