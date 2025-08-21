from django.urls import path
from . import views


urlspatterns = [
    path('brands/list', views.BrandListView.as_view(), name='brands_list')
]
