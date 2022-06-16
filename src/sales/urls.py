from django.urls import path
from .views import (
  home_view,
  SaleListView,
  SaleDetailsView,
)

app_name = 'sales'

urlpatterns = [
  path('', home_view, name = 'home'),
  path('sales/', SaleListView.as_view(), name = 'list'), #suer class.as_view() as it's a class view
  path('sales/<pk>', SaleDetailsView.as_view(), name = 'detail'),
]
