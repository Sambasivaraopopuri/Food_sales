from django.db import models

class Food_Sales(models.Model):
    date=models.DateField(blank=True,null=True)
    Region=models.CharField(max_length=255,blank=True,null=True)
    City=models.CharField(max_length=255,blank=True,null=True)
    Category=models.CharField(max_length=255,blank=True,null=True)
    Product=models.CharField(max_length=255,blank=True,null=True)
    Quantity=models.IntegerField(blank=True,null=True)
    UnitPrice=models.FloatField(blank=True,null=True)

    class Meta:
        db_table="Food_Sales"
