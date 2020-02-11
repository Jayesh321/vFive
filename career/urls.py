from django.conf.urls import url

from . import views

app_name='career'

urlpatterns = [
    url(r'^$', views.JobList.as_view(), name='all'),
    url(r'^create', views.CreateJobView.as_view(), name='job_create_url'),
    url(r'^(?P<pk>\d+)/', views.JobDetailView.as_view(), name='job_detail_url'),
    url(r'^update/(?P<pk>\d+)/', views.UpdateJobView.as_view(), name='job_update_url'),
    url(r'^delete/(?P<pk>\d+)/', views.DeleteJobView.as_view(), name='job_delete_url'),
    url(r'^apply_job/', views.CreateJobApplyView.as_view(), name='jobapply_url'),
    url(r'^upload/', views.upload, name='upload_url'),
]
