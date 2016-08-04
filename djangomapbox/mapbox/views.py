from django.shortcuts import render
from django.views.generic import View
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.conf import settings
from django.contrib.gis.db.models import Avg
from .models import outpointMD

def context_mapbox():
    """ 맵박스 토큰을 넘겨주기 위한 함수"""
    token = getattr(settings,'MAPBOX_TOKEN')
    return {'token':token}

# Create your views here.
class Index(View):
    def get(self,request,data=None):
        context = dict()
        gis = outpointMD.objects.all()
        point = gis.values('경도', '위도', '이름')
        center = gis.aggregate(Avg('경도'),Avg('위도'))
        context = {'point':point, 'center':center}
        context.update(context_mapbox())
        data = render_to_string("mapbox/index.html", context, request=request)
        return HttpResponse(data)
