from django.urls import path
from .views import product_list,product_spect


urlpatterns = [
    path('products/', product_list, name='product_list'),
    path('product_spect/<int:item_id>/', product_spect, name='product_spect'),
]
