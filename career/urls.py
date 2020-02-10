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



    #url(r'^registration/', views.RegistrationView, name='registration_url'),
    #url(r'^login/',auth_views.LoginView.as_view(template_name='career/login.html'), name='login_url'),
    #url(r'^logout/',auth_views.LogoutView.as_view(template_name='career/logout.html'), name='logout_url'),


    #url(r'^password_change/$',auth_views.PasswordChangeView.as_view(template_name='career/password_change.html'),
                     #name='password_change'),
    #url(r'^password_change/done/$',auth_views.PasswordChangeDoneView.as_view(template_name='career/password_change_done.html'),
                     #name='password_change_done'),
    #path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), 
                     #name='password_change'),



    #url(r'^password_reset/',auth_views.PasswordResetView.as_view(template_name='career/password_reset.html'),
                     #name='password_reset_url'),

    #url(r'^password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='career/password_reset_done.html'),
                     #name='password_reset_done_url'),

#url(r'^password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='career/password_reset_confirm.html'),
                     #name='password_reset_confirm_url'),
                     
    #url(r'^reset-password/confirm/(?P[0-9A-Za-z]+)-(?P.+)/$', password_reset_confirm, {'template_name': 'reset_password_confirm.html',
                    #'post_reset_redirect':'accounts:password_reset_complete'}, name='password_reset_confirm'),

    #url(r'password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='career/password_reset_complete.html'), 
                     #name='password_reset_complete'),
]
