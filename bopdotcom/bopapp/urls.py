from django.urls import path
from django.views.static import serve
from . import views
from django.conf import settings

urlpatterns = [
	path('', views.index, name='index'),
	path('bop', views.bop_someone, name='bopsomeone'),
	path('ajax/bop_someone/', views.bop_ajax, name='bop_ajax'),
	path('userpage/<int:u_id>/', views.user_page, name='userpage'),
	path('groups', views.groups, name='groups'),
	path('groups/<int:g_id>/', views.group_page, name='group_info'),
	path('login', views.login_user, name = 'login_user')
]