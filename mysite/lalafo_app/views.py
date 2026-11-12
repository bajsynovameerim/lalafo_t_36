from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import Category, Product
from .forms import ProductForms
from django.urls import reverse_lazy



class CategoryViews(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'category_list.html'


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    context_object_name = 'product'
    form_class = ProductForms
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'product_update.html'
    form_class = ProductForms
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


