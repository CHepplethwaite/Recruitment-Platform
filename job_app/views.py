from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import job
from django.utils.encoding import uri_to_iri



def home(request):
    return render(request,'job_app/index.html',{})

def about(request):
    return render(request,'job_app/site/about.html',{})

def career_advice(request):
    return render(request,'job_app/site/career_advice.html',{})

def contact(request):
    return render(request,'job_app/site/contact.html',{})

def education(request):
    return render(request,'job_app/site/education.html',{})

def legal(request):
    return render(request,'job_app/site/legal.html',{})

def payroll(request):
    return render(request,'job_app/site/payroll.html',{})

def post_job(request):
    return render(request,'job_app/site/post_job.html',{})

def recruitment(request):
    return render(request,'job_app/site/recruitment.html',{})

def submit_resume(request):
    return render(request,'job_app/site/submit_resume.html',{})

class jobListView(ListView):
    model = job
    paginate_by = 10




class jobDetailView(DetailView):
    model = job
    template_name = 'job_app/job_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'job_detail'

    def get_object(self, **kwargs):
        slug = self.kwargs.get('slug')
        return get_object_or_404(job, slug=uri_to_iri(slug))