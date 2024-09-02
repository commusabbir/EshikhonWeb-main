from django.db import models

# Create your models here.
class product(models.Model):
    title = models.CharField(max_length=50)
    describe = models.CharField(max_length=150)
    price = models.IntegerField(max_length=4)
    # link = models.CharField(max_length=50)
    def __str__ (self):
        return self.title
    