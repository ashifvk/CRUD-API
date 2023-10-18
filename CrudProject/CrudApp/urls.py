from django.urls import path
from . import views


urlpatterns = [
    path('AddProductApiView',views.AddProductApiView.as_view(),name='AddProductApiView'),
    path('GetAllProduct',views.GetAllProduct.as_view(),name='GetAllProduct'),
    path('DeleteProductApi/<int:id>',views.DeleteProductApi.as_view(),name='DeleteProductApi'),

]