from django.conf.urls import url

from crawlmanager.apps.foundation import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='hello'),
]