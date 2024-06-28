from django.urls import path
from products import views


urlpatterns = [
    path('products/', views.ProductAPIView.as_view({'post': 'list'}), name='products'),
]