from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import job
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
 


# site views

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

def recruitment(request):
    return render(request,'job_app/site/recruitment.html',{})

def submit_resume(request):
    return render(request,'job_app/site/submit_resume.html',{})

class jobListView(ListView):
    model = job
    paginate_by = 10
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
        return queryset


class jobDetailView(DetailView):
    model = job
    template_name = 'job_app/job_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'job_detail'

# category views

class academiaListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/academia.html'
    queryset=job.objects.filter(industry__exact="ACADEMIA", status__exact=f"{True}")
    


class adminListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/administration_list.html'
    queryset=job.objects.filter(industry__exact="ADMINISTRATION", status__exact=f"{True}")

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
        return queryset

class accountancyListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/accountancy_list.html'
    queryset=job.objects.filter(industry__exact="ACCOUNTANCY", status__exact=f"{True}")
  
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
        return queryset
   
    
class agricultureListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/agriculture_list.html'
    queryset=job.objects.filter(industry__exact="AGRICULTURE", status__exact=f"{True}")

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
        return queryset


class bankingListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/banking_and_finance.html'
    queryset=job.objects.filter(industry__exact="BANKING_AND_FINANCE", status__exact=f"{True}")

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
        return queryset


class developmentListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/development_list.html'
    queryset=job.objects.filter(industry__exact="DEVELOPMENT", status__exact=f"{True}")

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
        return queryset


class engineeringListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/engineering_and_construction_list.html'
    queryset=job.objects.filter(industry__exact="ENGINEERING_AND_CONSTRUCTION", status__exact=f"{True}")

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

        return queryset


class healthListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/health_list.html'
    queryset=job.objects.filter(industry__exact="HEALTH", status__exact=f"{True}")

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
        return queryset


class hrListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/human_resource_list.html'
    queryset=job.objects.filter(industry__exact="HUMAN_RESOURCE", status__exact=f"{True}")

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
        return queryset


class lawListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/legal_list.html'
    queryset=job.objects.filter(industry__exact="LAW", status__exact=f"{True}")

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
        return queryset


class manufacturingListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/manufacturing_list.html'
    queryset=job.objects.filter(industry__exact="MANUFACTURING_FMCG", status__exact=f"{True}")

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
        return queryset


class miscListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/other_list.html'
    queryset=job.objects.filter(industry__exact="OTHER", status__exact=f"{True}")

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
        return queryset


class retailListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/retail_and_sales.html'
    queryset=job.objects.filter(industry__exact="RETAIL_AND_SALES", status__exact=f"{True}")

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
        return queryset


class techListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/technology_list.html'
    queryset=job.objects.filter(industry__exact="ICT_AND_TELCO", status__exact=f"{True}")

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
        return queryset


class publicSectorListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/public_sector_list.html'
    queryset=job.objects.filter(industry__exact="PUBLIC_SECTOR", status__exact=f"{True}")

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
        return queryset


class transportListView(ListView):
    model = job
    paginate_by = 10
    ordering = ['-post_date']
    template_name = 'job_app/categories/transportation_and_logistics_list.html'
    queryset=job.objects.filter(industry__exact="TRANSPORT_AND_LOGISTICS", status__exact=f"{True}")

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
        return queryset


#career article views

def career_exploration(request):
    return render(request,'job_app/career_articles/career_exploration.html',{})

def education(request):
    return render(request,'job_app/career_articles/education.html',{})

def job_interviews(request):
    return render(request,'job_app/career_articles/job_interviews.html',{})

def job_market(request):
    return render(request,'job_app/career_articles/job_market.html',{})

def networking(request):
    return render(request,'job_app/career_articles/networking.html',{})

def salary(request):
    return render(request,'job_app/career_articles/salary_negotiations.html',{})

def self_assessment(request):
    return render(request,'job_app/career_articles/self_assessment.html',{})

def writing(request):
    return render(request,'job_app/career_articles/writing.html',{})

# view for filtering results



