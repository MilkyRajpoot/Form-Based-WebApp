from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('home/create/', views.create,name='create'),
    path('home/empanellist', views.list_view,name='list_view'),
    # url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^empanellist(?P<id>\d+)/$', views.detail_view,name='detail_view'),
    url(r'^empanellist(?P<id>\d+)/edit/$', views.update_view, name='update'),
    path('home/addmore/', views.addmore,name='addmore'),
    path('home/adddropdowncountry/', views.adddropdowncountry,name='adddropdowncountry'),
    path('home/adddropdownstate/', views.adddropdownstate,name='adddropdownstate'),
    path('home/adddropdowncity/', views.adddropdowncity,name='adddropdowncity'),
    path('home/adddropdownservice/', views.adddropdownservice,name='adddropdownservice'),
    path('home/adddropdownaccre/', views.adddropdownaccre,name='adddropdownaccre'),
    path('home/addauthperson/', views.addauthperson,name='addauthperson'),
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    # url(r'^uploads/$', views.model_form_upload, name='model_form_upload'),
    # url(r'^listDocument/$', views.listDocument, name='listDocument'),
    # url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
]
