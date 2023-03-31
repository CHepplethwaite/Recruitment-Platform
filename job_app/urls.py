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

]