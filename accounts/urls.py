from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns = [
    url(r'signup/$', views.SignUpView.as_view(template_name='accounts/signup.html'), name='signup_url'),
    #url(r'^registration/', views.RegistrationView, name='registration_url'),
    url(r'^login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login_url'),
    url(r'^logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout_url'),


    url(r'^password_change/$',auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
                     name='password_change'),
    url(r'^password_change/done/$',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
                     name='password_change_done'),
    #path('password-change/', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done')), 
                     #name='password_change'),



    url(r'^password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
                     name='password_reset_url'),

    url(r'^password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
                     name='password_reset_done_url'),

url(r'^password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
                     name='password_reset_confirm_url'),
                     
    #url(r'^reset-password/confirm/(?P[0-9A-Za-z]+)-(?P.+)/$', password_reset_confirm, {'template_name': 'reset_password_confirm.html',
                    #'post_reset_redirect':'accounts:password_reset_complete'}, name='password_reset_confirm'),

    url(r'password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), 
                     name='password_reset_complete'),
]
