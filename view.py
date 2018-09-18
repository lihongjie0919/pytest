from django.http import HttpResoponse
from django.shortcuts import redirect

def index(request):
	return HttpResponse('index')
