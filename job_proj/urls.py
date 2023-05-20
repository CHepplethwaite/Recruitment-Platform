from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("samisongo1986_ykw/", admin.site.urls),
    path("register/", user_views.register, name="register"),
    path("log-in/", auth_views.LoginView.as_view(template_name='users/login.html'), name="log_in"),
    path("log-out/", auth_views.LogoutView.as_view(template_name='users/logout.html'), name="log_out"),
    path('',include('job_app.urls')),
]
