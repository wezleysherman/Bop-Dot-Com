from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.http import JsonResponse

def index(request):
	user = request.user
	friends = Friend.objects.filter(Q(user1_id = user.id) | Q(user2_id = user.id)).values_list('user1_id', 'user2_id')
	friendBops = Bop_User.objects.filter(Q(userTo_id__in = [f for f in friends]) | Q(userFrom_id__in = [f for f in friends])).order_by('-bop__dateBopped')
	return render(request, 'mainpage.html', {
		'current_page': 'main',
		'name': 'Bop!',
		'bops': friendBops,
		'user': user
	})

def bop_someone(request):
	user = request.user
	friends = Friend.objects.filter(Q(user1_id = user.id) | Q(user2_id = user.id)).values_list('user1_id', 'user2_id')
	users = Profile.objects.filter(Q(user_id__in = [f for f in friends]))
	return render(request, 'bopsomeone.html', {
		'current_page': 'bop_someone',
		'name': 'Bop!',
		'friends': users,
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
