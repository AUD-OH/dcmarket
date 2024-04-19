from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from accounts.forms import RegisterForm
from accounts.models import User
from products.models import Product
from django import forms


def my_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success pacel
        return redirect(request.GET.get("next") or 'products:list')
    # Return an 'invalid login' error message.
    messages.error(request, "올바르지 않은 사용자 정보입니다.")
    return render(request, 'accounts/login.html')


def signup_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('products:list')
    context = {'form': form, }
    return render(request, 'accounts/signup.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next') or 'products:list')
        messages.error(request, "올바르지 않은 사용자 정보입니다.")
    return render(request, 'accounts/login.html')


@require_POST
def logout_view(request):
    logout(request)
    return redirect("product:list")


@login_required
@require_POST
def delete_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.author != request.user:
        messages.warning(request, '작성자 본인만 삭제 가능합니다.')
        return redirect("products:detail", product_id=product_id)
    product.delete()
    return redirect("products:list")




def profile_view(request, user_id):
    user = get_Object_or_404(User, id=user_id)
    return render(request, 'accounts/profile.html', {'profile_user': user})


@login_required
@require_POST
def follow_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if user.followers.filter(id=request.user.id).exists():
        user.followers.remove(request.user)
    else:
        user.followers.add(request.user)
    return redirect("accounts:profile", user_id=user_id)
