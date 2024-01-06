from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
        # add login and logout urls
    path('log-in/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('log-out/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
         name="password_reset"),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
         name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
         name="password_reset_confirm"),
    path('password-reset-complete/',
            auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
            name="password_reset_complete"),
    path('activate/<uidb64>/<token>/',
         user_views.activate, 
         name="activate"),
    # add register url
    path('register/', user_views.register, name="register"),
    # # add profile url
    path('account/', user_views.account, name="account"),
    path('update-account/', user_views.update_account, name="update_account"),
]