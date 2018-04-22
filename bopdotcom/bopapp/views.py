from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

def index(request):
	if(request.user.is_authenticated):
		user = request.user
		friends = Friend.objects.filter(Q(user1_id = Profile.objects.filter(user=user)[0].id) | Q(user2_id = Profile.objects.filter(user=user)[0].id)).values_list('user1_id', 'user2_id')
		friendBops = Bop_User.objects.filter(Q(userTo_id__in = [f[0] for f in friends]) | 
			Q(userTo_id__in = [f[1] for f in friends]) | Q(userFrom_id__in = [f[0] for f in friends]) | 
			Q(userFrom_id__in = [f[1] for f in friends])).order_by('-bop__dateBopped')
		return render(request, 'mainpage.html', {
			'current_page': 'main',
			'name': 'Bop!',
			'bops': friendBops,
			'user': user
		})
	else:
		return redirect('login_user')

def bop_someone(request):
	if(request.user.is_authenticated):
		user = request.user
		friends = Friend.objects.filter(Q(user1_id = Profile.objects.filter(user=user)[0].id) | Q(user2_id = Profile.objects.filter(user=user)[0].id)).values_list('user1_id', 'user2_id')
		users = Profile.objects.filter(Q(user_id__in = [f[0] for f in friends]) | Q(user_id__in = [f[1] for f in friends]))
		return render(request, 'bopsomeone.html', {
			'current_page': 'bop_someone',
			'name': 'Bop!',
			'friends': users,
			'user': user
		})
	else:
		return redirect('login_user')

def user_page(request, u_id):
	if(request.user.is_authenticated):
		user = User.objects.filter(id = u_id)[0]
		cuser = request.user
		friends = Friend.objects.filter(Q(user1_id = Profile.objects.filter(user=user)[0].id) | Q(user2_id = Profile.objects.filter(user=user)[0].id)).values_list('user1_id', 'user2_id')
		friend_users = Profile.objects.filter(Q(user_id__in = [f[0] for f in friends]) | Q(user_id__in = [f[1] for f in friends]))
		achievements = Has_Achievement.objects.filter(user_id = Profile.objects.filter(user=user)[0].id)
		groups = In_Group.objects.filter(user_id = Profile.objects.filter(user=user)[0].id)
		return render(request, 'userpage.html', {
			'current_page': 'profile',
			'achievements': achievements,
			'groups': groups,
			'name': 'Bop!',
			'friends': friend_users,
			'user_view': user,
			'user': cuser
		})
	else:
		return redirect('login_user')

def groups(request):
	if(request.user.is_authenticated):
		user = request.user
		groups = In_Group.objects.filter(user_id = Profile.objects.filter(user=user)[0].id)
		groups_joined = In_Group.objects.filter(user_id = Profile.objects.filter(user=user)[0].id).values_list("group")
		groups_not_joined = In_Group.objects.exclude(user_id = Profile.objects.filter(user=user)[0].id).exclude(group__in = groups_joined).values_list("group", flat = True).distinct()
		groups_not_joined_list = Group.objects.filter(id__in = groups_not_joined)

		return render(request, 'groupspage.html', {
			'current_page': 'group',
			'name': 'Bop!',
			'groups': groups,
			'groups_not_joined' : groups_not_joined_list,
			'user': user
		})
	else:
		return redirect('login_user')

def group_page(request, g_id):
	if(request.user.is_authenticated):
		user = request.user
		groups = Group.objects.filter(id=g_id)[0]
		people_in_group = In_Group.objects.filter(group = g_id).values_list('user', flat=True)
		people = Profile.objects.filter(user_id__in = people_in_group)
		return render(request, 'groupinfo.html', {
			'current_page': 'group',
			'name': 'Bop!',
			'group': groups,
			'people': people,
			'user': user
		})
	else:
		return redirect('login_user')

def bop_ajax(request):
	if request.user.is_authenticated:
		profile = request.user.profile
		bopped_user = Profile.objects.filter(user_id=request.POST.get('friend'))
		mess = request.POST.get('msg')
		nbop = Bop.objects.create(message=mess)
		nbop.save()
		bopped_user = Bop_User.objects.create(bop=nbop, userFrom=profile, userTo=bopped_user[0])
		bopped_user.save()
		return JsonResponse({'return': 'success'})
	else:
		return Http404()

def login_user(request):
	return render(request, 'login.html', {'current_page': 'login', 'name': 'login'})

def ajax_register(request):
	# Create a new user, give them some friends and groups, then authenticate and log them in.
	new_user = User.objects.create_user(username=request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
	new_user.save()
	first_friend = Friend.objects.create(user2=Profile.objects.filter(user=new_user)[0], user1=Profile.objects.filter(userName="wezdawg")[0])
	first_friend.save()
	first_friend = Friend.objects.create(user2=Profile.objects.filter(user=new_user)[0], user1=Profile.objects.filter(userName="ZacTheMan")[0])
	first_friend.save()
	first_friend = Friend.objects.create(user2=Profile.objects.filter(user=new_user)[0], user1=Profile.objects.filter(userName="swaguire")[0])
	first_friend.save()
	first_bop = Bop_User.objects.create(bop=Bop.objects.all()[0], userTo=Profile.objects.filter(user=new_user)[0], userFrom=Profile.objects.all()[0])
	first_bop.save()
	first_group = In_Group.objects.create(group=Group.objects.all()[0], user=Profile.objects.filter(user=new_user)[0])
	first_group.save()
	authed_user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
	login(request, authed_user)

	return redirect('index')

def ajax_login(request):
	authed_user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
	print(authed_user)
	if(authed_user):
		login(request, authed_user)
		return redirect('index')
	else:
		return JsonResponse({'return': 'err'})

def ajax_logout(request):
	logout(request)
	return redirect('index')

def register_user(request):
	return render(request, 'register.html', {'current_page': 'register', 'name': 'Register!'})

def join_group(request):
	if request.user.is_authenticated:
		profile = request.user.profile
		group = Group.objects.filter(id=request.POST.get('id'))
		joined_group = In_Group.objects.create(user=profile, group=group[0])
		joined_group.save()
		return JsonResponse({'return': 'success'})
	else:
		return Http404()
