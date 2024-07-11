# Import necessary modules
from django.db import models
from django.shortcuts import render
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

# Django settings
settings.configure(DEBUG=True, SECRET_KEY='your_secret_key')

# Define the Django model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

# Define a view to display a list of products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Define URL patterns
urlpatterns = [
    path('products/', product_list, name='product_list'),
]

# Define a simple HTML template
template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Product List</title>
</head>
<body>
    <h1>Product List</h1>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - ${{ product.price }}</li>
        {% endfor %}
    </ul>
</body>
</html>
'''

# Add the template to the templates directory
with open('templates/product_list.html', 'w') as f:
    f.write(template)

# Configure the Django application
from django.core.management import execute_from_command_line
execute_from_command_line(['manage.py', 'runserver'])
