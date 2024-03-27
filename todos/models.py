from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 200,null = False)
    due_date = models.DateField()
    
