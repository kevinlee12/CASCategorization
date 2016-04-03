# pylint: disable=invalid-name
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^categories/(?P<category>\w+)', views.CategoryJSONView.as_view(),
        name='activity_type'),
]
