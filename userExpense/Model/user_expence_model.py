from django.db import models 
from Category.Model.category_model import CategoryModel 
from User.models import User 

from django.utils import timezone


class UserExpenseModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    expense_date = models.DateField(default=timezone.now)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 

    def __str__(self):
        return f"{self.user.username} - {self.category.title} - {self.amount}"
    

    class Meta:
        db_table = "UserExpenseModel"
        verbose_name = "User Expense"
        verbose_name_plural = "User Expenses"