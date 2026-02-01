from rest_framework import serializers 
from ..Model.user_expence_model import UserExpenseModel
from Category.Serializer.category_serializer import CategorySerializer
from User.Serializer.user_serializer import UserProfileSerializer



class CreateUserExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserExpenseModel
        fields = '__all__'




class GetUserExpenseSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True,many=False)
    category = CategorySerializer(read_only=True,many=False)

    class Meta:
        model = UserExpenseModel
        fields = '__all__'