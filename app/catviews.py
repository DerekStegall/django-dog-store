

def cat_product_detail(request, cat_product_id):
    cat_product = CatProduct.objects.get(id=cat_product_id)
    return render(request, "cat_product_detail.html", {"cat_product": cat_product})


def purchase_detail(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    return render(request, "purchase_detail.html", {"purchase": purchase})


def cat_tag_list(request):
    cat_tags = CatTag.objects.all()
    return render(request, "cat_tag_list.html", {"cat_tags": cat_tags})


def purchase_cat_product(request, cat_product_id):
    cat_product = CatProduct.objects.get(id=cat_product_id)
    if cat_product.quantity > 0:
        cat_product.quantity = cat_product.quantity - 1
        cat_product.save()
        purchase = cat_product.purchase_set.create()
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

