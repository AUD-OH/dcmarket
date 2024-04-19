from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST

from products.forms import ProductForm
from products.models import Product


# Create your views here.

@login_required
def update_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if product.author != request.user:
        messages.warning(request, '본인만 수정 가능합니다.')
        return redirect("products:detail", product_id=product_id)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST':
        if form.is_valid():
            form.save(author=request.user)
            return redirect("products:list")
    return render(request, "products/create.html", {"form": form})

def list_view(request):
    # list_view
    # 리스트를 보여줘야
    product_instance_list = Product.objects.all()
    return render(request, "products/list.html", {"product_instance_list": product_instance_list})

@login_required
def create_view(request):
    form = ProductForm(author=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, author = request.user)
        if form.is_valid():
            form.save()
            return redirect("products:list")
    return render(request, "products/create.html",{"form": form})

def detail_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "products/detail.html", {"product": product})


@login_required
@require_POST
def delete_view(request, product_id):
    product = get_object_or_404(product, id=product_id)
    if product.author != request.user:
        messages.warning(request, '작성자 본인만 삭제 가능합니다.')
        return redirect("products:detail", product_id=product_id)
    product.delete()
    return redirect("products:list")


@login_required
@require_POST
def jjim_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user: User = request.user
    if user.jjim_products.filter(id=product_id).exists():
        user.jjim_products.remove(product)
    else:
        user.jjim_products.add(product)
    return redirect("products:list")
