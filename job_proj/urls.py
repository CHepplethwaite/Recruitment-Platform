from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from job_app import views as job_app_views


urlpatterns = [
    path("samisongo1986_ykw/", admin.site.urls),
    path('',include('job_app.urls')),
    path('users/', include('users.urls')),
    path('admin-panel/', include('jobs.urls')),
]
