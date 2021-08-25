from django.urls import path
from .views import ProductsList, ProductDetail, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductSearch

urlpatterns = [

    path('', ProductsList.as_view()),
    path('<int:pk>', ProductDetail.as_view(), name = 'post_detail'),
    path('create/', ProductCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', ProductUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='post_delete'),
    path('post_search/', ProductSearch.as_view()),

]