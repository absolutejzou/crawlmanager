from django.conf.urls import url

from crawlmanager.apps.foundation import views

app_name = 'foundation'
urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^login$', views.sign_in, name='login'),
    url(r'^logout$', views.sign_out, name='logout'),
]
