from django.db import models 

from User.models import User 
from Category.Model.category_model import CategoryModel 
from django.utils import timezone 




class UserExpencesModel(models.Model):

    user= models.ForeignKey(User,related_name='user_expence',on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel,related_name='expence_category',on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6,decimal_places=2)
    expire_date= models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"expence id : {self.id}"

