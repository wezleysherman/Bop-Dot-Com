from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib.auth import authenticate
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from datetime import datetime
import subprocess
import os
from shutil import copyfile
import codecs
import sys

def index(request):
	user = request.user
	return render(request, 'index.html', {
		'current_page': 'index',
		'name': 'Bop!',
		'user': user
	})