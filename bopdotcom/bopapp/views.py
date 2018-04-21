from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import JsonResponse

def index(request):
	user = request.user
	friends = Friend.objects.filter(Q(user1_id = user.id) | Q(user2_id = user.id)).values_list('user1_id', 'user2_id')
	friendBops = Bop_User.objects.filter(Q(userTo_id__in = [f[0] for f in friends]) | 
		Q(userTo_id__in = [f[1] for f in friends]) | Q(userFrom_id__in = [f[0] for f in friends]) | 
		Q(userFrom_id__in = [f[1] for f in friends])).order_by('-bop__dateBopped')
	return render(request, 'mainpage.html', {
		'current_page': 'main',
		'name': 'Bop!',
		'bops': friendBops,
		'user': user
	})

def bop_someone(request):
	user = request.user
	friends = Friend.objects.filter(Q(user1_id = user.id) | Q(user2_id = user.id)).values_list('user1_id', 'user2_id')
	users = Profile.objects.filter(Q(user_id__in = [f[0] for f in friends]) | Q(user_id__in = [f[1] for f in friends]))
	return render(request, 'bopsomeone.html', {
		'current_page': 'bop_someone',
		'name': 'Bop!',
		'friends': users,
		'user': user
	})

def user_page(request, u_id):
	user = User.objects.filter(id = u_id)[0]
	cuser = request.user
	friends = Friend.objects.filter(Q(user1_id = user.id) | Q(user2_id = user.id)).values_list('user1_id', 'user2_id')
	friend_users = Profile.objects.filter(Q(user_id__in = [f[0] for f in friends]) | Q(user_id__in = [f[1] for f in friends]))
	achievements = Has_Achievement.objects.filter(user_id = user.id)
	groups = In_Group.objects.filter(user_id = user.id)
	return render(request, 'userpage.html', {
		'current_page': 'profile',
		'achievements': achievements,
		'groups': groups,
		'name': 'Bop!',
		'friends': friend_users,
		'user_view': user,
		'user': cuser
	})

def groups(request):
	user = request.user
	groups = In_Group.objects.filter(user_id = user.id)
	groups_joined = In_Group.objects.filter(user_id = user.id).values_list("group")
	groups_not_joined = In_Group.objects.exclude(user_id = user.id).exclude(group__in = groups_joined).values_list("group", flat = True).distinct()
	groups_not_joined_list = Group.objects.filter(id__in = groups_not_joined)

	return render(request, 'groupspage.html', {
		'current_page': 'group',
		'name': 'Bop!',
		'groups': groups,
		'groups_not_joined' : groups_not_joined_list,
		'user': user
	})

def group_page(request, g_id):
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

def join_group(request):
	if request.user.is_authenticated:
		profile = request.user.profile
		group = Group.objects.filter(id=request.POST.get('id'))
		joined_group = In_Group.objects.create(user=profile, group=group[0])
		joined_group.save()
		return JsonResponse({'return': 'success'})
	else:
		return Http404()
