from rest_framework.viewsets import ModelViewSet 
from ..Model.user_expence_model import UserExpenseModel
from ..Serializer.user_expance_serializer import CreateUserExpenseSerializer,GetUserExpenseSerializer



class UserExpenseViewSet(ModelViewSet):
    
    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return GetUserExpenseSerializer
        return CreateUserExpenseSerializer
    
    def get_queryset(self):

        user=self.request.user

        queryset = UserExpenseModel.objects.filter(
            is_deleted=False
            ).select_related('category','user').order_by('-created_at')


        if user.is_admin:

            return  queryset
          
        return  queryset.filter(user=user)
     