from django.shortcuts import render
from . import models
from django.shortcuts import redirect
from . import forms as user_forms
from django.contrib import messages
from .decorators import user_not_authenticated
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from .token import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMessage


def user_list(request):
    """
    Retrieve a list of users.
    """
    users = models.User.objects.all()
    return render(request, 'users/user_list.html', {'users': users})


def user_detail(request, pk):
    """
    Retrieve details of a specific user.
    """
    user = models.User.objects.get(pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})

def user_create(request):
    """
    Create a new user.
    """
    if request.method == 'POST':
        form = user_forms.UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = user_forms.UserForm()
    return render(request, 'users/user_form.html', {'form': form})

def user_edit(request, pk):
    """
    Edit an existing user.
    """
    user = models.User.objects.get(pk=pk)
    if request.method == 'POST':
        form = user_forms.UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = user_forms.UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

def user_delete(request, pk):
    """
    Delete a user.
    """
    models.User.objects.get(pk=pk).delete()
    return redirect('user_list')

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")
    return redirect('homepage')


def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("users/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.warning(request, f'Dear {user}, please go to your email ({to_email}) inbox and click on \
                the received activation link to confirm and complete your registration. Note: Check your \
                     spam folder if you cannot see the email.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


@user_not_authenticated
def register(request):
    if request.method == 'POST':
        form = user_forms.UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            username = form.cleaned_data['username']
            messages.success(request, f'Your account has been created, {username}! Please activate it.')
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = user_forms.UserRegisterForm()
    return render(
        request=request, 
        template_name='users/register.html', 
        context={'form': form},
        )


@login_required
def update_account(request):
    if request.method == 'POST':
        u_form = user_forms.UserUpdateForm(request.POST, instance=request.user)
        a_form = user_forms.AccountUpdateForm(request.POST, request.FILES, instance=request.user.account)
        if u_form.is_valid() and a_form.is_valid():
            u_form.save()
            a_form.save()
            messages.success(request, f'Account updated!')
            return redirect('account')
    else:
        u_form = user_forms.UserUpdateForm(instance=request.user)
        a_form = user_forms.AccountUpdateForm(instance=request.user.account)

    context = {
        'u_form': u_form,
        'a_form': a_form,
    }
    return render(request, 'users/account_update.html', context)

@login_required
def account(request):
    return render(request, 'users/account.html', {})

    

