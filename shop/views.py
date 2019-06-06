from django.shortcuts import *
from django.http import *
from django.contrib.auth.models import User
from .models import Product, CartTable
from shop.forms import ShopForm
from django.views.decorators.csrf import csrf_exempt


def index(request):
    featured_products = Product.objects.all().filter(is_featured=True)
    context = {
        "products": featured_products
    }
    return render(request,'shop/index.html',context)


def all_products(request):
    product = Product.objects.all()
    context ={
        "products": product
    }
    return render(request, 'shop/products.html', context)


def product(request, product_id):
    product_detail = Product.objects.get(id=product_id)
    category = product_detail.category_name
    related_products = Product.objects.all().filter(category_name=category)
    products = CartTable.objects.all().filter(userid_id = request.user.id)
    context = {
        "product": product_detail,
        "products": related_products,
        "cartTable": products,
        }
    return render(request, 'shop/productdetail.html', context)


def view_cart(request):
    subtotal = 0
    products = CartTable.objects.all().filter(userid_id = request.user.id)
    for item in products:
        subtotal += item.product.price * item.qty
    context = {"cartTable" : products,
            "subtotal": subtotal}
    return render(request, 'shop/cart.html', context)

@csrf_exempt
def addtocartaction(request):
    if request.method == 'POST':
        pid = int(request.POST['id'])
        qty = int(request.POST['qty'])
        print(pid, qty)
        
        if User.is_authenticated:
            product1 = Product.objects.get(id=pid)
            user = User.objects.get(id=request.user.id)
            if CartTable.objects.filter(product_id=product1.id).exists():
                data = CartTable.objects.get(product_id=product1.id)
                data.qty += 1  
                data.save()
                print("Quatity Incremented")
                ar = {"Reply":1}
                return JsonResponse(ar, safe=False)     
            else:
                print("Create Block")   
                cart = CartTable.objects.create(product=product1, qty=qty, userid=user)
                cart.save()
                ar = {"Reply":1}
                return JsonResponse(ar, safe=False)
        else:
            print("Anonoymas ")
            # if request.session.has_key('cartlist'):
            #     cartlist = request.session['cartlist']
            #     x = {'pid': pid, 'qty': qty}
            #     cartlist.append(x)

            # cartlist = []
            # x = {'pid': pid, 'qty': qty}
            # cartlist.append(x)
            # request.session['cartlist'] = cartlist
            return redirect("")
    else:
        print("GET block")
        return HttpResponseRedirect("products")

@csrf_exempt
def upcartaction(request):
    pid = int(request.POST['id'])
    obj = CartTable.objects.get(product_id = pid)
    obj.qty += 1
    obj.save()
    return JsonResponse("Quantity Updated", safe=False)

@csrf_exempt
def downcartaction(request):
    pid = int(request.POST['id'])
    obj = CartTable.objects.get(product_id = pid)
    if obj.qty >= 1:
        obj.qty -= 1
        obj.save()
        obj = CartTable.objects.get(product_id = pid)
        if obj.qty == 0:
            CartTable.objects.filter(product_id=pid).delete()
        
    return JsonResponse("Quantity Updated", safe=False)


def demo(request):
    form = ShopForm()

    if request.method == 'POST':
        form = ShopForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    context = {'form': form}
    return render(request,"shop/formpage.html", context)

