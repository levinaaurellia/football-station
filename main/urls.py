from django.urls import path
from main.views import show_main, add_product, product_detail, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_product, delete_product, get_product_json_by_id
from main.views import get_products_json, add_product_ajax, edit_product_ajax, delete_product_ajax, login_user_ajax, register_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add/product/', add_product, name="add_product"),
    path('products/<str:id>/', product_detail, name='product_detail'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'),
    
    # AJAX URLs
    path('get-products/', get_products_json, name='get_products_json'),
    path('add-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('edit-product-ajax/<uuid:id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete-product-ajax/<uuid:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('login-ajax/', login_user_ajax, name='login_ajax'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('get-product/<uuid:id>/', get_product_json_by_id, name='get_product_json_by_id'),
]