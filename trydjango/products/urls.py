from django.urls import path
from .views import(
    product_list_view,
    product_detail_view,
    product_delete_view,
    product_create_view,
    dynamic_lookup_view
)


app_name = 'products'
urlpatterns = [
    path('create/', product_create_view),
    
    path('<int:my_id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:my_id>/delete/', product_delete_view, name = 'product-delete'),
    path('', product_list_view)
]