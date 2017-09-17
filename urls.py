from django.conf.urls import url
from . import views   
urlpatterns = [
# url(r'^$', views.index), # This line has changed!
url(r'^$', views.index),
url(r'^processform$', views.processform),
url(r'^results/$', views.results),
url(r'^test$', views.test),
]