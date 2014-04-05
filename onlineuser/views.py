import json
from django.http import HttpResponse
from django.shortcuts import render
from onlineuser.models import getOnlineInfos

def get_online_users(request):
	res = getOnlineInfos(detail=True, json=True)
	response = json.dumps(res, ensure_ascii=False)
	return HttpResponse(response, content_type="application/json")