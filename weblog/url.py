from django.urls import path 
from . import views


urlpatterns = [
    path('' ,views.WeblogListView.as_view(), name='weblog'),
    path('<slug:slug>/', views.weblogDetailsView.as_view(), name='weblog_detail'),
]