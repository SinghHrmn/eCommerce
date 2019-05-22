from django.shortcuts import *
from django.http import *
from django.contrib.auth.models import User
from .models import products,carttable
from shop.forms import ShopForm


def index(request):
    featured_products = products.objects.all().filter(is_featured=True)
    context = {
        "products": featured_products
    }
    return render(request,'shop/index.html',context)


def all_products(request):
    product = products.objects.all()
    context ={
        "products": product
    }
    return render(request, 'shop/products.html', context)


def product(request, product_id):
    product_detail = products.objects.get(id=product_id)
    category = product_detail.category_name
    related_products = products.objects.all().filter(category_name=category)
    context = {
        "product": product_detail,
        "products": related_products
    }
    return render(request, 'shop/productdetail.html', context)


def view_cart(request):
    return render(request, 'shop/cart.html')


def addtocartaction(request):
    pid = int(request.GET['pid'])
    qty = int(request.GET['qty'])
    if User.is_authenticated:
        cart = carttable(pid=pid, qty=qty, userid=request.user.id)
        cart.save()
        return redirect(request.path)
    else:
        if request.session.has_key('cartlist'):
            cartlist = request.session['cartlist']
            x = {'pid': pid, 'qty': qty}
            cartlist.append(x)

        cartlist = []
        x = {'pid': pid, 'qty': qty}
        cartlist.append(x)
        request.session['cartlist'] = cartlist
        return redirect(request.path)



def demo(request):
    form = ShopForm()

    if request.method == 'POST':
        form = ShopForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    context = {'form': form}
    return render(request,"shop/formpage.html", context)

