from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.




class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.PositiveIntegerField(validators = [MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.code