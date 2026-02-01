from django.contrib import admin

# Register your models here.

from .Model.user_expence_model import UserExpenseModel  


admin.site.register(UserExpenseModel)
