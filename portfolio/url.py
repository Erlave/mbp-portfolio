from django.urls import path 
from . import views


urlpatterns = [
    path('' ,views.portfolioListView.as_view(), name='port'),
    path('<slug:slug>/', views.PortfolioDetailsView.as_view(), name='portfolio_detail'),
]