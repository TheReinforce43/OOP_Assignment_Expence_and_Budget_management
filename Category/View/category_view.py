from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from rest_framework import status 
from Category.Model.category_model import CategoryModel
from Category.Serializer.category_serializer import CategorySerializer


class CategoryModelViewSet(ModelViewSet):

    serializer_class=CategorySerializer
    queryset=CategoryModel.objects.all()