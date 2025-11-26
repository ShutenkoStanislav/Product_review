from django.shortcuts import render
from reviews.models import Review, Product

def home(request):
    return render(request, template_name="review/home.html")

def product_list(request):
    products = Product.objects.all()
    context = {
        "products" : products
    }

    return render(request, template_name="review/product_list.html", context=context)


#  • Форма повинна дозволяти ввести автора,
# текст відгуку та рейтинг.

#  • Після подання форми, відгук зберігається 
# у базі даних.

#  • Під формою відображаються всі відгуки
# на цей продукт.