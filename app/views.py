from django.shortcuts import render, redirect
from app.models import (
    DogProduct,
    Purchase,
    DogTag,
    CatProduct,
    PurchaseCatProduct,
    CatTag,
)
from app.forms import NewDogTagForm, NewCatTagForm
from django.contrib import messages


def home(request):
    dog_products = DogProduct.objects.all()
    return render(
        request,
        "home.html",
        {"dog_products": dog_products})

def cat_store(request):
    cat_products = CatProduct.objects.all()
    return render(
        request,
        "cat_store.html",
        {"cat_products": cat_products})

def dog_product_detail(request, dog_product_id):
    dog_product = DogProduct.objects.get(id=dog_product_id)
    return render(request, "dog_product_detail.html", {"dog_product": dog_product})


def purchase_detail(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    return render(request, "purchase_detail.html", {"purchase": purchase})


def dog_tag_list(request):
    dog_tags = DogTag.objects.all()
    return render(request, "dog_tag_list.html", {"dog_tags": dog_tags})


def purchase_dog_product(request, dog_product_id):
    dog_product = DogProduct.objects.get(id=dog_product_id)
    if dog_product.quantity > 0:
        dog_product.quantity = dog_product.quantity - 1
        dog_product.save()
        purchase = dog_product.purchase_set.create()
        messages.success(request, f"Purchased {dog_product.name}")
        return redirect("purchase_detail", purchase.id)
    else:
        messages.error(request, f"{dog_product.name} is out of stock")
        return redirect("dog_product_detail", dog_product.id)


def new_dog_tag(request):
    if request.method == "GET":
        return render(request, "new_dog_tag.html")
    else:
        form = NewDogTagForm(request.POST)
        if form.is_valid():
            owner_name = form.cleaned_data["owner_name"]
            dog_name = form.cleaned_data["dog_name"]
            dog_birthday = form.cleaned_data["dog_birthday"]
            dog_tag = DogTag.objects.create(
                owner_name=owner_name, dog_name=dog_name, dog_birthday=dog_birthday
            )
            return redirect("dog_tag_list")
        else:
            return render(request, "new_dog_tag.html", {"form": form})



def cat_product_detail(request, cat_product_id):
    cat_product = CatProduct.objects.get(id=cat_product_id)
    return render(request, "cat_product_detail.html", {"cat_product": cat_product})

def cat_tag_list(request):
    cat_tags = CatTag.objects.all()
    return render(request, "cat_tag_list.html", {"cat_tags": cat_tags})


def purchase_cat_product(request, cat_product_id):
    cat_product = CatProduct.objects.get(id=cat_product_id)
    if cat_product.quantity > 0:
        cat_product.quantity = cat_product.quantity - 1
        cat_product.save()
        purchase = cat_product.purchasecatproduct_set.create()
        messages.success(request, f"Purchased {cat_product.name}")
        return redirect("purchase_detail", purchase.id)
    else:
        messages.error(request, f"{cat_product.name} is out of stock")
        return redirect("cat_product_detail", cat_product.id)


def new_cat_tag(request):
    if request.method == "GET":
        return render(request, "new_cat_tag.html")
    else:
        form = NewCatTagForm(request.POST)
        if form.is_valid():
            owner_name = form.cleaned_data["owner_name"]
            cat_name = form.cleaned_data["cat_name"]
            cat_birthday = form.cleaned_data["cat_birthday"]
            cat_tag = catTag.objects.create(
                owner_name=owner_name, cat_name=cat_name, cat_birthday=cat_birthday
            )
            return redirect("cat_tag_list")
        else:
            return render(request, "new_cat_tag.html", {"form": form})

