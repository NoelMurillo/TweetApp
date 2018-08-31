
from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$', views.tweet_list_view, name='list'),
    url(r'^1/$', views.tweet_detail_view, name='detail'),
]
