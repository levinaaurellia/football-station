from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from main.models import Product
from main.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt 
from django.views.decorators.http import require_POST  
import json  


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
def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "add_product.html", context)

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

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
       return HttpResponse(status=404)
   
def show_json_by_id(request, product_id):
    try:
       product_item = Product.objects.get(pk=product_id)
       json_data = serializers.serialize("json", [product_item])
       return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
       return HttpResponse(status=404)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    news = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=news)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))



def get_products_json(request):
    filter_type = request.GET.get('filter', 'all')
    
    if filter_type == 'my':
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()

    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'stock': product.stock,
            'brand': product.brand,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def add_product_ajax(request):
    try:
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        thumbnail = request.POST.get("thumbnail")
        category = request.POST.get("category")
        brand = request.POST.get("brand")
        stock = request.POST.get("stock")
        is_featured = request.POST.get("is_featured") == 'on'

        new_product = Product(
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            brand=brand,
            stock=stock,
            is_featured=is_featured,
            user=request.user
        )
        new_product.save()

        return JsonResponse({'status': 'success', 'message': 'Product added successfully!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def edit_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        
        # Check if user owns the product
        if product.user != request.user:
            return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)

        product.name = request.POST.get("name")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.thumbnail = request.POST.get("thumbnail")
        product.category = request.POST.get("category")
        product.brand = request.POST.get("brand")
        product.stock = request.POST.get("stock")
        product.is_featured = request.POST.get("is_featured") == 'on'
        
        product.save()

        return JsonResponse({'status': 'success', 'message': 'Product updated successfully!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
@require_POST
@login_required(login_url='/login')
def delete_product_ajax(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        
        # Check if user owns the product
        if product.user != request.user:
            return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)

        product.delete()
        return JsonResponse({'status': 'success', 'message': 'Product deleted successfully!'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

@csrf_exempt
def login_user_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            # Validasi
            if not username or not password:
                return JsonResponse({'status': 'error', 'message': 'Username and password are required'}, status=400)
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response_data = {'status': 'success', 'message': 'Login successful!'}
                response = JsonResponse(response_data)
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid username or password'}, status=400)
                
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password1 = data.get('password1')
            password2 = data.get('password2')
            
            # Validasi
            if not username or not password1 or not password2:
                return JsonResponse({'status': 'error', 'message': 'All fields are required'}, status=400)
            
            if password1 != password2:
                return JsonResponse({'status': 'error', 'message': 'Passwords do not match'}, status=400)
            
            if User.objects.filter(username=username).exists():
                return JsonResponse({'status': 'error', 'message': 'Username already exists'}, status=400)
            
            # Create user
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            
            return JsonResponse({'status': 'success', 'message': 'Registration successful! You can now login.'})
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def get_product_json_by_id(request, id):
    try:
        product = get_object_or_404(Product, pk=id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': f"Rp{product.price:,}", # Format price with commas
            'description': product.description,
            'thumbnail': product.thumbnail if product.thumbnail else '{% static "images/no-image.png" %}', # Add a placeholder
            'category': product.get_category_display(),
            'brand': product.get_brand_display(),
            'stock': f"Stock: {product.stock}",
            'user_username': product.user.username if product.user else "Admin",
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)