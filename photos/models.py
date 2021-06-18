from django.db import models
from django.urls import reverse


class Photos(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('photo', kwargs={'photo_id': self.pk})

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


