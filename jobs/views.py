from django.shortcuts import render
from job_app.models import job
from django import forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy

# job list view
class jobListView(ListView):
    model = job
    template_name = 'jobs/job_list.html'
    context_object_name = 'jobs'
    ordering = ['-post_date']

# job detail view
class jobDetailView(DetailView):
    model = job
    template_name = 'jobs/job_detail.html'
 
# job create view 
class jobCreateView(LoginRequiredMixin, CreateView):
    description = forms.CharField()
    model = job
    template_name = 'jobs/job_form.html'
    fields = ['job_title','organisation','url','email','closing_date','district','province','industry','details',]
    widgets = {
        'job_title': forms.TextInput(attrs={'class': 'form-control'}),
        'organisation': forms.TextInput(attrs={'class': 'form-control'}),
        'url': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'closing_date': forms.DateInput(attrs={'class': 'form-control'}),
        'district': forms.TextInput(attrs={'class': 'form-control'}),
        'province': forms.TextInput(attrs={'class': 'form-control'}),
        'industry': forms.TextInput(attrs={'class': 'form-control'}),
        'details': forms.Textarea(attrs={'class': 'form-control'}),
        'logo': forms.FileInput(attrs={'class': 'form-control'}),
    }
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# job update view
class jobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = job
    template_name = 'jobs/job_form.html'
    fields = ['job_title','organization','url','email','closing_date','district','province','industry','details',]
    widgets = {
        'job_title': forms.TextInput(attrs={'class': 'form-control'}),
        'organization': forms.TextInput(attrs={'class': 'form-control'}),
        'url': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'closing_date': forms.DateInput(attrs={'class': 'form-control'}),
        'district': forms.TextInput(attrs={'class': 'form-control'}),
        'province': forms.TextInput(attrs={'class': 'form-control'}),
        'industry': forms.TextInput(attrs={'class': 'form-control'}),
        'details': forms.Textarea(attrs={'class': 'form-control'}),
        'logo': forms.FileInput(attrs={'class': 'form-control'}),
    }

    def form_valid(self, form):
        form.instance.user = self.request.user.username
        return super().form_valid(form)
    
    def test_func(self):
        job = self.get_object()
        if self.request.user.username == job.user:
            return True
        return False


# job delete view
class jobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job_list')

    def test_func(self):
        job = self.get_object()
        if self.request.user.username == job.author:
            return True
        return False


@login_required
def jobs_approval(request):
    jobs = job.objects.all().order_by('-post_date')
    if request.user.is_staff:
        if request.method == 'POST':
            checked_ids = request.POST.getlist('boxes')
            jobs_to_approve = job.objects.filter(id__in=checked_ids)
            jobs_to_approve.update(approved=True)
            messages.success(request, f'jobs approved!')
            return redirect('jobs_approval')
        return render(request, 'jobs/jobs_approval.html', {'jobs': jobs})
    else:
        messages.warning(request, f'You do not have permission to view this page.')
        return redirect('home')