from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import job
from django.utils.encoding import uri_to_iri


# site views

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
    ordering = ['-post_date']

class jobDetailView(DetailView):
    model = job
    template_name = 'job_app/job_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'job_detail'

    def get_object(self, **kwargs):
        slug = self.kwargs.get('slug')
        return get_object_or_404(job, slug=uri_to_iri(slug))

class academiaListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/academia.html'

class adminListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/administration_list.html'

class accountancyListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/accountancy_list.html'
    
class agricultureListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/agriculture_list.html'

class bankingListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/banking_and_finance.html'
    
class developmentListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/development_list.html'

class engineeringListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/engineering_and_construction_list.html'

class healthListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/health_list.html'

class hrListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/human_resource_list.html'

class lawListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/legal_list.html'
    
class manufacturingListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/manufacturing_list.html'
    
class miscListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/other_list.html'
    
class retailListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/retail_and_sales.html'

class techListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/technology_list.html'

class publicSectorListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/technology_list.html'

class transportListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/transportation_and_logistics_list.html'

    
    