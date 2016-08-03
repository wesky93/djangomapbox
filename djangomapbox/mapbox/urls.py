from django.conf.urls import url,patterns
from mapbox import views

urlpatterns = patterns('',
                       # 인덱스 페이지 (블로그 메인 페이지)
                       url(r'^$',views.Index.as_view(),name='index'),
                       )