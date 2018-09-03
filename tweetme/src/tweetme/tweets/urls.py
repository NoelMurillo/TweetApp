
from . import views
from django.conf.urls import url
from django.urls import path

app_name = ['tweet']
urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', views.TweetListView.as_view(), name='list'),
    url(r'^create/$', views.TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.TweetDeleteView.as_view(), name='delete'),
]
