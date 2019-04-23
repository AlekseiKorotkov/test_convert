from django.urls import path,re_path
from . import views


urlpatterns = [
    path('', views.show),
    re_path(r'my_ajax_request/$', views.convert_numbers)
]