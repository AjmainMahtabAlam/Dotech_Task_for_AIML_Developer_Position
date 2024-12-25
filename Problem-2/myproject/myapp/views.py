from django.shortcuts import render
from .models import Category
from django.db.models import Sum, Count
from django.http import HttpResponse

def homepage(request):
    return HttpResponse('''
        <h1>Welcome to My App</h1>
        <p>Use the links below to navigate:</p>
        <ul>
            <li><a href="/myapp/top-categories/">View Top Categories</a></li>
        </ul>
    ''')


def top_categories_view(request):
    # Aggregating total price and counting products for each category
    categories = (Category.objects
                  .annotate(total_price=Sum('product__price'),
                            product_count=Count('product'))
                  .filter(total_price__isnull=False)  # Exclude categories without products
                  .order_by('-total_price')[:5])  # Get top 5 categories by total price

    # Format the categories for the template
    context = {
        "categories": [
            {
                "category_name": category.name,
                "total_price": float(category.total_price),
                "product_count": category.product_count
            }
            for category in categories
        ]
    }
    return render(request, 'myapp/top_categories.html', context)
