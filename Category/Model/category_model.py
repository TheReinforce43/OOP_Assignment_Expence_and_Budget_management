from django.db import models 


class CategoryModel(models.Model):

    title=models.CharField(max_length=250,unique=True,db_index=True)
    description = models.TextField(null=True,blank=True)
    is_delete=models.BooleanField(default=False) 
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"category title : {self.title}"
    
    class Meta:
        db_table='CategoryModel'
    
    