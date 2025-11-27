from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from reviews.models import Review, Product

def home(request):
    return render(request, template_name="review/home.html")

def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, template_name="review/product_list.html", context=context)


def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        author = request.POST.get("author")  
        text = request.POST.get("text")
        rating = request.POST.get("rating")

        review = Review.objects.create(
            product=product,  
            author=author,    
            text=text,
            rating=rating,
        )
        return redirect("product_details", pk=review.id)
    else:
        context = {"product": product}
        return render(request, template_name="review/add_view.html", context=context)


def product_details(request, pk):  
    try:
        review = Review.objects.get(id=pk)  
        context = {
            "review": review  
        }
        return render(request, template_name="review/product_details.html", context=context)
    except Review.DoesNotExist:
        return HttpResponse("This review doesn't exist", status=404)