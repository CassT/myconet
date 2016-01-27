from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^groups/', views.groups, name='groups'),
    url(r'^about/', views.about, name='about'),
    url(r'^events/', views.events, name='events'),
]

