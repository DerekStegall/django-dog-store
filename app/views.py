from django.shortcuts import render, redirect
from app.models import DogProduct, Purchase, DogTag
from app.forms import NewDogTagForm
from django.contrib import messages


def home(request):
    dog_products = DogProduct.objects.all()
    return render(request, "home.html", {"dog_products": dog_products})


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
    specific_id = DogProduct.objects.get(id=dog_product_id)
    if specific_id.quantity > 0:
        specific_id.quantity = specific_id.quantity - 1
        specific_id.save()
        purchase = specific_id.purchase_set.create()
        messages.success(request, f"Purchased {specific_id.name}")
        return redirect("purchase_detail", purchase.id)
    else:
        messages.error(request, f"{specific_id.name} is out of stock")
        return redirect("dog_product_detail", specific_id.id)


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
