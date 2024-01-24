from django.urls import path
from . import views as job_views

urlpatterns = [
    path('create-job/', job_views.jobCreateView.as_view(), name="create_job"),
    path('<int:pk>/delete/', job_views.jobDeleteView.as_view(), name="delete_job"),
    path('<int:pk>/edit-job/', job_views.jobUpdateView.as_view(), name="edit_job"),
    path('', job_views.jobsListView.as_view(), name="job_list_admin_panel"),
    path('<int:pk>/', job_views.jobsDetailView.as_view(), name="job_detail_admin_panel"),
    path('jobs-approval/', job_views.jobs_approval, name="jobs_approval"),
]