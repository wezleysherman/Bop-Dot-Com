from django.urls import path
from django.views.static import serve
from . import views
from django.conf import settings

urlpatterns = [
	path('', views.index, name='index'),
	path('bop', views.bop_someone, name='bopsomeone'),
	path('ajax/bop_someone/', views.bop_ajax, name='bop_ajax')
]