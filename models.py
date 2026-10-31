from django.db import models
class slide(models.Model):
    slide_img = models.FileField(upload_to="slide/",max_length=100,null=True,default=None)
    slide_img2 = models.FileField(upload_to="slide/",max_length=100,null=True,default=None)
    slide_img3 = models.FileField(upload_to="slide/",max_length=100,null=True,default=None)
    slide_text = models.CharField(max_length=50)
    slide_text2 = models.CharField(max_length=50)
    slide_img4 = models.FileField(upload_to="slide/",max_length=100,null=True,default=None)
    slide_text3 = models.CharField(max_length=50)
    
# Create your models here.
