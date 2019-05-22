from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mrp = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    additional_info = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_on_sale = models.BooleanField(default=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    category_name = models.ForeignKey('category', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'Products'


class category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class carttable(models.Model):
    pid = models.ForeignKey(products,on_delete=models.DO_NOTHING)
    qty = models.IntegerField()
    userid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    mobile_number = models.CharField(max_length=20)
    address = models.TextField()
    payment_method = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = 'carttable'




