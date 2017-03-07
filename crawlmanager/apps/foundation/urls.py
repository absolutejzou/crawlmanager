from django.conf.urls import url

from crawlmanager.apps.foundation import views

app_name = 'foundation'
urlpatterns = [
    url(r'^$', views.Home.as_view(), name='hello'),
    url(r'^test/(?P<pk>[0-9]+)$', views.Test.as_view(), name='test'),
    url(r'^signup$', views.Signup.as_view(), name='signup'),
    url(r'^login$', views.Login.as_view(), name='login'),
    url(r'^logout$', views.Logout.as_view(), name='logout'),
]
