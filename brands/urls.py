from django.urls import path
from . import views


urlpatterns = [
    path('brands/list/', views.BrandListView.as_view(), name='brands_list'),
    path('brands/list/', views.CreateView.as_view(), name='brands_create'),
]
