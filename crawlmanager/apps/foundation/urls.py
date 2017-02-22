from django.conf.urls import url

from crawlmanager.apps.foundation import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='hello'),
    url(r'^test/(\d+)$', views.Test.as_view(), name='test'),
]