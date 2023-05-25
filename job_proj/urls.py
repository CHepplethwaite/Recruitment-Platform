from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from job_app import views as job_app_views
from posts.admin import tumpe_admin_site

urlpatterns = [
    path("samisongo1986_ykw/", admin.site.urls),
    path("sign-up/", user_views.register, name="register"),
    path('manage-jobs/', tumpe_admin_site.urls),
    path("log-in/", auth_views.LoginView.as_view(template_name='users/login.html'), name="log_in"),
    path("log-out/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name="log_out"),
    path("paasword-reset/", auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name="password_reset"),
    path('',include('job_app.urls')),
]
