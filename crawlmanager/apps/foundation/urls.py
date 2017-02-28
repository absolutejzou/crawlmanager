from django.conf.urls import url

from crawlmanager.apps.foundation import views

app_name = 'foundation'
urlpatterns = [
    url(r'^$', views.Home.as_view(), name='hello'),
    url(r'^test/(?P<pk>[0-9]+)$', views.Test.as_view(), name='test'),
]
