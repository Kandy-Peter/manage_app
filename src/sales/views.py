from django.shortcuts import render
from django.views.generic import ListView, DetailView
import pandas as pd
from .models import Sale
from .forms import SalesSearchForm
# Create your views here.

def home_view(request):
  sales_df = None
  form = SalesSearchForm(request.POST or None)
  if request.method == 'POST':
    date_from = request.POST.get('date_from')
    date_to = request.POST.get('date_to')
    chart_type = request.POST.get('chart_type')
    print(date_from, date_to, chart_type)

    qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from) #__lte: created date less than or equal to date_to
    
    if len(qs) > 0:
      print("#################")
      sales_df =  pd.DataFrame(qs.values())
      
      #to avoid ambiguous truth value of dataframe

      sales_df = sales_df.to_html()
      print(sales_df)
    else:
      print('no data')
  # generate the context dictionary
  context = {
    'form': form,
    'sales_df': sales_df,
  }
  return render(request, 'sales/home.html', context)

class SaleListView(ListView):
  model = Sale
  template_name = 'sales/main.html'
  # I can object_context_name = "sale" and this will overide the 'object_list' in main.html

class SaleDetailsView(DetailView):
  model = Sale
  template_name = 'sales/detail.html'
