from itertools import product
from os import name
from venv import create

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryViews, ProductListView, ProductDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView

urlpatterns = [
    path('category/', CategoryViews.as_view(), name='category_list'),
    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(),name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

