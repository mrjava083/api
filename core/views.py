from django.shortcuts import render
from random import choice
from django.http import JsonResponse
from .models import Mega
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
# Create your views here.
def tmpGeneration(N, S):
	for i in range(N): S += choice([*"abcdefghijklmnopqrstuvwxyz"])
	return S
def checkInput(P, T):
	try:
		for i in T:P.POST[i]
		Mega(title=P.POST['title'], slug=tmpGeneration(48, ''), body=P.POST['body']).save()
		return {'status' : 'OK'}
	except: return {'status' : 'ERROR_INPUT'}
def checkValues(M):
	try:
		this_slug = M.POST['slug']
		try:
			this_q = Mega.objects.get(slug=this_slug)
			return {'status' : 'OK', 'data' : {'title' : this_q.title, 'body' : this_q.body}}
		except: return {'status' : 'ERROR_VALUES'}
	except:return {'status' : 'ERROR_INPUT'}
####################################################################################################
@csrf_exempt
@require_POST
def newObject(request):
	return JsonResponse(checkInput(request,['title', 'body']))
@require_GET
def listObject(request):
	temp = []
	for i in Mega.objects.all():temp.append({'title':i.title, 'slug':i.slug})
	return JsonResponse({'status' : 'OK', 'data' : temp})
@csrf_exempt
@require_POST
def getObject(request):
	return JsonResponse(checkValues(request))