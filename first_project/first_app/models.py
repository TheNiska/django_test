from django.db import models


# Create your models here.
class MenuCategory(models.Model):
    category_name = models.CharField(max_length=200)


class MenuItem(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT,
                                    default=None, related_name='category')


class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time!")
