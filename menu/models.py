from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=55)
    submenu = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
