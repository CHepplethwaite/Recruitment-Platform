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
    path('academia/',job_views.academiaListView.as_view(),name="academia"),
    path('accountancy/',job_views.accountancyListView.as_view(),name="accountancy"),
    path('administration',job_views.adminListView.as_view(),name="admin"),
    path('agriculture/' ,job_views.agricultureListView.as_view(),name="agric"),
    path('banking_and_finance',job_views.bankingListView.as_view(),name="banking"),
    path('development',job_views.developmentListView.as_view(),name="dev"),
    path('engineering_and_construction',job_views.engineeringListView.as_view(),name="eng" ),
    path('health/',job_views.healthListView.as_view(),name="health"),
    path('human_resource/',job_views.hrListView.as_view(),name="HR"),
    path('law/',job_views.lawListView.as_view(),name="law"),
    path('manufacturing/',job_views.manufacturingListView.as_view(),name="manufacturing"),
    path('miscellaneous/',job_views.miscListView.as_view(),name="misc"),
    path('public_sector/',job_views.publicSectorListView.as_view(),name="public_sector"),
    path('retail/',job_views.retailListView.as_view(),name="retail"),
    path('technology/',job_views.techListView.as_view(),name="technology"),
    path('transportation_and_logistics/',job_views.transportListView.as_view(),name="transport"),

    #job article urls
    path('career-advice/career-exploration/',job_views.career_exploration,name="exploration"),
    path('career-advice/education-and-training/',job_views.education,name="education"),
    path('career-advice/job-interview-skills/',job_views.job_interviews,name="interviews"),
    path('career-advice/job-market-trends/',job_views.job_market,name="job_market"),
    path('career-advice/networking/',job_views.networking,name="networking"),
    path('career-advice/salary-negotiations/',job_views.salary,name="salary"),
    path('career-advice/self-assessment/',job_views.self_assessment,name="self_assessment"),
    path('career-advice/resume-and-cover-letter-writing/',job_views.writing,name="writing"),
]