from django.db import models
from django.db.models import Max , Sum , Avg , Min 

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
    
    def no_of_ratings(self):
        return Rating.objects.filter(meal = self.id).count()
        
    def avg_rating(self):
        sum = Rating.objects.filter(meal = self.id).aggregate(Sum('stars'))['stars__sum']
        no_of_rate = self.no_of_ratings()
        if  no_of_rate == 0:    
            return 0
        else:
            return sum / no_of_rate
    
    # To enter a particuler item using (uuid or slug)
    
    # By slug 
    # def save(self ,*args ,**kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
    
    # By id 
    # id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

        
class Rating(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1) , MaxValueValidator(5)])
    

    class Meta:
        unique_together = (('user' , 'meal'))
