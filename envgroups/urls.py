from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^signup_complete/', views.signup_complete, name='signup_complete'),
#    url(r'^groups/', views.groups, name='groups'),
    url(r'^groups/(?P<group_id>[0-9]+)/', views.groups, name='groups'),
    url(r'^groups/', views.groups, name='groups'),
    url(r'^about/', views.about, name='about'),
    url(r'^events/', views.events, name='events'),
]

