from django.conf.urls import url
from . import views

app_name='pragati'

urlpatterns = [
    url(r'^home/', views.HomeView.as_view(), name= 'home_url'),
    url(r'^idea/', views.IdeaCreateView.as_view(), name='idea_url'),
    url(r'^list/', views.IdeaListView.as_view(), name='list_url'),
    url(r'^(?P<pk>\d+)/', views.IdeaDetailView.as_view(), name='detail_url'),
    url(r'^like/', views.Idea_Like, name= 'like_url'),
        
]

