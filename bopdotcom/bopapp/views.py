from django.shortcuts import render
from .models import *
from django.db.models import Q

def index(request):
	user = request.user
	friends = Friend.objects.filter(Q(user1_id = user.id), Q(user2_id = user.id)).values_list('user1_id', flat=True)
	friendBops = Bop_User.objects.filter(Q(userTo_id__in = friends), Q(userFrom_id__in = friends))
	return render(request, 'mainpage.html', {
		'current_page': 'index',
		'name': 'Bop!',
		'bops': friendBops,
		'user': user
	})