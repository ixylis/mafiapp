from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^player/(?P<playername>\w+)/$', views.playerprofile, name='playerprofile'),
    url(r'^item/(?P<itemid>\w+)/$', views.itemprofile, name='itemprofile'),
    url(r'^ability/(?P<abilityid>\w+)/$', views.abilityprofile, name='abilityprofile'),
    url(r'^attribute/(?P<attributeid>\w+)/$', views.attributeprofile, name='attributeprofile'),


]
