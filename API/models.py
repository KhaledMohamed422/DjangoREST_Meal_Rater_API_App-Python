from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
import uuid

# Create your models here.

class Meal(models.Model):
    
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=300)
    # slug = models.SlugField(null=True , blank=True)
    
   
    # To enter a particuler item using (uuid or slug)
    
    # By slug 
    # def save(self ,*args ,**kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    
    # By id 
    # id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

        
    
class Guest(models.Model):    
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Rating(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    user = models.ForeignKey(Guest,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5)])
    

    class Meta:
        unique_together = (('user' , 'meal'))
    # index_together = (('user', 'meal'),)