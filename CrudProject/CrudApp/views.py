from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import product
from .serializers import productSerializer
# Create your views here.

class AddProductApiView(GenericAPIView):
    serializer_class=productSerializer
    def post(self,request):
        name=request.data.get('name')
        price=request.data.get('price')
        category=request.data.get('category')
        count=request.data.get('count')
        serializer=self.serializer_class(data={'name':name,'price':price,'category':category,'count':count})
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'message':'produc added successfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':serializer.errors,'message':'Failed','success':False},status=status.HTTP_400_BAD_REQUEST)
    

class GetAllProduct(GenericAPIView):
    def get(self,request):
        query=product.objects.all()
        if(query.count()>0):
            serializer=productSerializer(query,many=True)
            return Response({'data':serializer.data,'message':'All product get successfully','success':True},status=status.HTTP_201_CREATED)
        return Response({'data':'no data available','success':False},status=status.HTTP_400_BAD_REQUEST)
    

class DeleteProductApi(GenericAPIView):
    def delete(self,request,id):
        query=product.objects.get(id=id)
        query.delete()
        return Response({'message':'Deleted successfully','success':True},status=status.HTTP_201_CREATED)
    

    

        
