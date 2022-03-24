from django.db import models

# Create your models here.
class Students(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=100)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=100)
    comment  = models.CharField(max_length=100,default="not available")


