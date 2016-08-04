import os
from django.contrib.gis.utils import LayerMapping
from .models import outpointMD
outpointmd_mapping = {
    '경도' : '경도',
    '위도' : '위도',
    '이름' : '이름',
    'geom' : 'POINT',
}

outpointMD_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', '무등산 표주매설위치.shp'),)

def run(verbose=True):
    lm = LayerMapping(
        outpointMD, outpointMD_shp, outpointmd_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)