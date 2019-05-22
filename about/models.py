from django.db import models

class aboutus(models.Model):
    description = models.TextField()
    aboutus_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    def __str__(self):
        return self.description
    class Meta:
        verbose_name_plural = 'About Us'