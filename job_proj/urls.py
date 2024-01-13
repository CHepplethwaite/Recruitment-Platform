from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from job_app import views as job_app_views
from posts.admin import tumpe_admin_site
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("samisongo1986_ykw/", admin.site.urls),
    path('manage-jobs/', tumpe_admin_site.urls),
    path('',include('job_app.urls')),
    path('users/', include('users.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
