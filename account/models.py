from django.db import models
from django.utils.timezone import now

# Create your models here.
class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    short_paragraph = models.CharField(max_length=10000)
    news_paragraph_1 = models.TextField()
    news_paragraph_2 = models.TextField(blank="True",default="")
    news_paragraph_3 = models.TextField(blank="True",default="")
    Categoary = models.CharField(max_length=1000,blank="True",default="")
    timestamp = models.DateTimeField(default=now)
    image1 = models.ImageField(upload_to='pics',blank=True,null=True)
    image3 = models.ImageField(upload_to='pics',blank=True,null=True)
    image4 = models.ImageField(upload_to='pics',blank=True,null=True)

class join_us(models.Model):
    image = models.ImageField(upload_to='pics', blank=True, null=True)


class E_Magazine(models.Model):
    id = models.AutoField(primary_key=True)
    magazine_cover = models.ImageField(upload_to='e-magzine')
    magazine = models.FileField(upload_to='e-magzine')

