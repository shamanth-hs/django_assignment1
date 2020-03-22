from django.db import models

# Create your models here.

class Categories(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to ="categories/images",blank = True)

    def __str__(self):
        return self.title

class Items(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length=500)
    cost = models.DecimalField(max_digits= 10,decimal_places = 3,default=10)
    features = models.TextField(default="higly recomended")
    image = models.ImageField(upload_to ="webapp/images",blank = True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)

    def __str__(self):
        return self.title