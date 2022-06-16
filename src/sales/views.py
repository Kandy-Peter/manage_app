from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale

# Create your views here.

def home_view(request):
  hello = 'Hello world from the view'
  return render(request, 'sales/home.html', {'hello': hello})

class SaleListView(ListView):
  model = Sale
  template_name = 'sales/main.html'
  # I can object_context_name = "sale" and this will overide the 'object_list' in main.html

class SaleDetailsView(DetailView):
  model = Sale
  template_name = 'sales/detail.html'