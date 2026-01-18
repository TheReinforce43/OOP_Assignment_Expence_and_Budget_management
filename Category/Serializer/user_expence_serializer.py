from rest_framework import serializers 
from Category.Model.user_expence_model import UserExpencesModel
from Category.Serializer.category_serializer import CategorySerializer 
from User.Serializer.user_serializer import UserProfileSerializer 



class Create_User_Expence_serializer(serializers.ModelSerializer):

    class Meta:

        model=UserExpencesModel
        fields='__all__'



class Get_User_Expence_serializer(serializers.ModelSerializer):

    user=UserProfileSerializer(many=False,read_only=True)
    category= CategorySerializer(read_only=True,many=False)

    class Meta:

        model=UserExpencesModel
        fields='__all__'


        




