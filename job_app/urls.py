from django.urls import path
from . import views as job_views

urlpatterns =[
    path('',job_views.jobListView.as_view(), name='job_list'),
    # path('jobs/',job_views.jobListView.as_view(), name='job-list'),
    path('detail/<slug:slug>/', job_views.jobDetailView.as_view(),name="job_detail"),
    path('about/', job_views.about, name="about"),
    path('career_advice/', job_views.career_advice, name="career_advice"),
    path('contact/', job_views.contact, name="contact"),
    path('education/',job_views.education, name="education"),
    path('legal/', job_views.legal, name="legal"),
    path('payroll/', job_views.payroll, name="payroll"),
    path('post_job/', job_views.post_job, name="post_job"),
    path('recruitment/', job_views.recruitment, name="recruitment"),
    path('submit_resume/', job_views.submit_resume, name="submit_resume"),
   
   # category urls
    path('academia/',job_views.education,name="academia"),
    path('accountancy/',job_views.accountancy_list,name="accountancy"),
    path('administration',job_views.administration_list,name="admin"),
    path('agriculture/' ,job_views.agriculture_list),
    path('banking_and_finance',job_views.banking_and_finance_list,name="banking"),
    path('development',job_views.development_list,name="dev"),
    path('engineering_and_construction',job_views.engineering_and_construction_list,name="eng" ),
    path('health/',job_views.health_list,name="health"),
    path('human_resource/',job_views.human_resource_list,name="HR"),
    path('legal/',job_views.legal_list,name="legal"),
    path('manufacturing/',job_views.manufacturing_list,name="manufacturing"),
    path('miscellaneous/',job_views.other_list,name="misc"),
    path('public_sector/',job_views.public_sector_list,name="public_sector"),
    path('retail/',job_views.retail_and_sales_list,name="retail"),
    path('technology/',job_views.technology_list,name="technology"),
    path('transportation_and_logistics/',job_views.transportation_and_logistics_list,name="transport"),
]