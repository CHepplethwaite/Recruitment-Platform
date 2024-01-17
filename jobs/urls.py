from django.urls import path
from . import views as job_views

urlpatterns = [
    path('jobs/create-job/', job_views.jobCreateView.as_view(), name="create_job"),
    path('jobs/<int:pk>/delete/', job_views.jobDeleteView.as_view(), name="delete_job"),
    path('jobs/<int:pk>/update/', job_views.jobUpdateView.as_view(), name="edit_job"),
    path('jobs/', job_views.jobListView.as_view(), name="job_list_admin_panel"),
    path('jobs/<int:pk>/', job_views.jobDetailView.as_view(), name="job_detail_admin_panel"),
    path('jobs-approval/', job_views.jobs_approval, name="jobs_approval"),
]