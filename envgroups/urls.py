from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^signup/', views.signup_view, name='signup'),
    url(r'^signup_complete/', views.signup_complete, name='signup_complete'),
#    url(r'^groups/', views.groups, name='groups'),
    url(r'^projects/', views.projects, name='projects'), 
    url(r'^groups/(?P<group_id>[0-9]+)/', views.groups, name='groups'),
    url(r'^groups/', views.groups, name='groups'),
    url(r'^about/', views.about, name='about'),
    url(r'^blog/', views.blog, name='blog'),
    url(r'^events/', views.events, name='events'),
    url(r'^create_profile/', views.create_profile, name="create_profile"),
    url(r'^profile_created/', views.profile_created, name="profile_created"),
    url(r'^profile/(?P<username>.*)/', views.profile, name='profile'),
    url(r'^profile/', views.profiles, name='profiles'),
    url(r'^edit_profile/(?P<username>.*)/', views.edit_profile, name='edit_profile'),
    url(r'^projects2/', views.projects2, name='projects2'),
#    url(r'^projects/', views.projects, name='projects'),
]

