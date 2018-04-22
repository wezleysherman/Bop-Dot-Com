from django.urls import path
from django.views.static import serve
from . import views
from django.conf import settings

urlpatterns = [
	path('', views.index, name='index'),
	path('bop', views.bop_someone, name='bopsomeone'),
	path('ajax/bop_someone/', views.bop_ajax, name='bop_ajax'),
	path('ajax/join_group/', views.join_group, name='join_group'),
	path('userpage/<int:u_id>/', views.user_page, name='userpage'),
	path('groups', views.groups, name='groups'),
	path('groups/<int:g_id>/', views.group_page, name='group_info'),
	path('login', views.login_user, name = 'login_user'),
	path('ajax/register_ajax/', views.ajax_register, name='register_user_ajax'),
	path('ajax/login_ajax/', views.ajax_login, name='login_user_ajax'),
	path('ajax/logout/', views.ajax_logout, name='logout_user_ajax'),
	path('register', views.register_user, name='register_user')
]