from django.urls import path
from . import views as job_views

urlpatterns =[
    path('',job_views.jobListView.as_view(), name='job_list'),
    # path('jobs/',job_views.jobListView.as_view(), name='job-list'),
    path('job-details/<int:pk>/', job_views.jobDetailView.as_view(),name="job_detail"),
    path('about/', job_views.about, name="about"),
    path('career-advice/', job_views.career_advice, name="career_advice"),
    path('contact/', job_views.contact, name="contact"),
    path('education/',job_views.education, name="education"),
    path('legal/', job_views.legal, name="legal"),
   
   # category urls
    path('job-categories/academia-and-research/',job_views.academiaListView.as_view(),name="academia"),
    path('job-categories/accountancy/',job_views.accountancyListView.as_view(),name="accountancy"),
    path('job-categories/administration/',job_views.adminListView.as_view(),name="admin"),
    path('job-categories/agriculture/' ,job_views.agricultureListView.as_view(),name="agric"),
    path('job-categories/banking-and-finance/',job_views.bankingListView.as_view(),name="banking"),
    path('job-categories/development/',job_views.developmentListView.as_view(),name="dev"),
    path('job-categories/engineering-and-construction/',job_views.engineeringListView.as_view(),name="eng" ),
    path('job-categories/health/',job_views.healthListView.as_view(),name="health"),
    path('job-categories/human-resource/',job_views.hrListView.as_view(),name="HR"),
    path('job-categories/law/',job_views.lawListView.as_view(),name="law"),
    path('job-categories/manufacturing-and-fmcg/',job_views.manufacturingListView.as_view(),name="manufacturing"),
    path('job-categories/miscellaneous/',job_views.miscListView.as_view(),name="misc"),
    path('job-categories/public-sector/',job_views.publicSectorListView.as_view(),name="public_sector"),
    path('job-categories/retail-and-sales/',job_views.retailListView.as_view(),name="retail"),
    path('job-categories/technology/',job_views.techListView.as_view(),name="technology"),
    path('job-categories/transportation-and-logistics/',job_views.transportListView.as_view(),name="transport"),

    #job article urls
    path('career-advice/career-exploration/',job_views.career_exploration,name="exploration"),
    path('career_advice/education-and-training/',job_views.education,name="education"),
    path('career-advice/job-interviewing-skills/',job_views.job_interviews,name="interviews"),
    path('career-advice/job-market-trends/',job_views.job_market,name="job_market"),
    path('career-advice/networking/',job_views.networking,name="networking"),
    path('career-advice/negotiation-and-salary/',job_views.salary,name="salary"),
    path('career-advice/self-assessment/',job_views.self_assessment,name="self_assessment"),
    path('career-advice/resume-and-cover-letter-writing/',job_views.writing,name="writing"),
    
    #downloads
    
    path('download-privacy-policy-pdf/',job_views.download_pdf,name="privacy_policy"),
    path('search-results/', job_views.SearchView.as_view(), name='search_jobs'),
]