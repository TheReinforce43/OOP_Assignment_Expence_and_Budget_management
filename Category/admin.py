from django.contrib import admin
from Category.Model.category_model import CategoryModel 
from Category.Model.user_expence_model import UserExpencesModel


admin.site.register(CategoryModel)
admin.site.register(UserExpencesModel)
