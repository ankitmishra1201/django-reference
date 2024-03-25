from django.db import models

# Create your models here.

class Topic(models.Model):
    top_name=models.CharField(max_length=256,unique=True)

    def __str__(self):
        return self.top_name
    

    

