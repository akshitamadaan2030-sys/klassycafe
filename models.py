from django.db import models
class week(models.Model):
    week_img = models.FileField(upload_to="week/",max_length=100,null=True,default=None)
    week_name = models.CharField(max_length=50)
    week_des = models.CharField(max_length=100)
    week_price = models.CharField(max_length=50)
# Create your models here.
