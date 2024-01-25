from django.shortcuts import render
from job_app.models import job
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import JobForm



class jobsListView(ListView, UserPassesTestMixin, LoginRequiredMixin):
    model = job
    paginate_by = 10
    template_name = 'jobs/job_list.html'
    ordering = ['-post_date']
    queryset=job.objects.filter(status__exact=f"{True}")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location_choices = job.location_choices
        location_choices = [{'value': value, 'label': label} for value, label in location_choices]
        context["locations"] = location_choices
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        location = self.request.GET.get('location')
        if location:
            queryset = queryset.filter(location=location)
        return queryset.filter(user=self.request.user)
    
    def test_func(self):
        job = self.get_object()
        if self.request.user == job.user:
            return True
        return False


class jobsDetailView(DetailView):
    model = job
    template_name = 'jobs/job_detail.html'
    context_object_name = 'job'


# job create view 
class jobCreateView(LoginRequiredMixin, CreateView):
    model = job
    template_name = 'jobs/job_form.html'
    form_class = JobForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# job update view
class jobUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = job
    template_name = 'jobs/job_form.html'
    form_class = JobForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        job = self.get_object()
        if self.request.user == job.user:
            return True
        return False


# job delete view
class jobDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = job
    template_name = 'jobs/job_confirm_delete.html'
    success_url = reverse_lazy('job_list_admin_panel')

    def test_func(self):
        job = self.get_object()
        if self.request.user == job.user:
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
    
    
    