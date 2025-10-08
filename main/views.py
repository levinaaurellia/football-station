from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.contrib.auth.models import User



@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'app_name' : 'Football Station',
        'name': 'Levina Aurellia',
        'class': 'PBP D',
        'npm': '2406356776',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
@csrf_exempt
@require_POST
def add_product(request):
    name = strip_tags(request.POST.get("name") or "")
    price = request.POST.get("price") or "0"
    description = strip_tags(request.POST.get("description") or "")
    thumbnail = request.POST.get("thumbnail") or ""
    category = request.POST.get("category") or "jersey"
    is_featured = (request.POST.get("is_featured") == 'on')
    stock = int(request.POST.get("stock") or 0)
    brand = request.POST.get("brand") or "adidas"

    p = Product(
        name=name,
        price=int(price),
        description=description,
        thumbnail=thumbnail,
        category=category,
        is_featured=is_featured,
        stock=stock,
        brand=brand,
        user=request.user if request.user.is_authenticated else None,
    )
    p.save()
    return JsonResponse({'ok': True, 'product': _product_to_dict(p)}, status=201)


@login_required(login_url='/login')
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

# Data delivery
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


#  Helper serializer 
def _product_to_dict(p: Product):
    return {
        'id': str(p.pk),
        'name': p.name,
        'price': p.price,
        'description': p.description,
        'thumbnail': p.thumbnail,
        'category': p.category,
        'is_featured': p.is_featured,
        'stock': p.stock,
        'brand': p.brand,
        'user_id': p.user.id if p.user else None, 
        'username': p.user.username if p.user else None,
    }


def show_json(request):
    qs = Product.objects.all().order_by('-pk')  # bebas
    data = [_product_to_dict(p) for p in qs]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
    try:
        p = Product.objects.get(pk=product_id)
        return JsonResponse(_product_to_dict(p))
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        if not username or not password or not password2:
            return JsonResponse({'ok': False, 'error': 'All fields are required'}, status=400)
        if password != password2:
            return JsonResponse({'ok': False, 'error': 'Passwords do not match'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'ok': False, 'error': 'Username already exists'}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'ok': True, 'username': user.username}, status=201)
    
    return render(request, 'register.html')

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({'ok': True, 'username': user.username})
        return JsonResponse({'ok': False, 'error': 'Invalid credentials'}, status=400)
    
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login_user'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@require_POST
def edit_product(request, product_id):
    try:
        p = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        return JsonResponse({'ok': False, 'error': 'Not found'}, status=404)

    name = strip_tags(request.POST.get("name") or p.name)
    price = request.POST.get("price") or p.price
    description = strip_tags(request.POST.get("description") or p.description)
    thumbnail = request.POST.get("thumbnail") or p.thumbnail
    category = request.POST.get("category") or p.category
    is_featured = (request.POST.get("is_featured") == 'on') if ('is_featured' in request.POST) else p.is_featured
    stock = int(request.POST.get("stock") or p.stock)
    brand = request.POST.get("brand") or p.brand

    p.name = name
    p.price = int(price)
    p.description = description
    p.thumbnail = thumbnail
    p.category = category
    p.is_featured = is_featured
    p.stock = stock
    p.brand = brand
    p.save()

    return JsonResponse({'ok': True, 'product': _product_to_dict(p)})

@csrf_exempt
@require_POST
def delete_product(request, product_id):
    try:
        p = Product.objects.get(pk=product_id)
        p.delete()
        return JsonResponse({'ok': True})
    except Product.DoesNotExist:
        return JsonResponse({'ok': False, 'error': 'Not found'}, status=404)

