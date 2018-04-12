from django.urls import path
from django.views.static import serve
from . import views
from django.conf import settings

urlpatterns = [
	path('', views.index, name='index')
]