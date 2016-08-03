from django.shortcuts import render
from django.views.generic import View
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings

def context_mapbox():
    """ 맵박스 토큰을 넘겨주기 위한 함수"""
    token = getattr(settings,'MAPBOX_TOKEN')
    return {'token':token}

# Create your views here.
class Index(View):
    def get(self,request,data=None):
        context = dict()
        context.update(context_mapbox())
        data = render_to_string("mapbox/index.html", context, request=request)
        return HttpResponse(data)

