from django.db import models


# Create your models here.

# Relationships examples

# One-to-One -----------------------------------------------------------------
class College(models.Model):
    college_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    website = models.URLField()


class Principal(models.Model):
    college_id = models.OneToOneField(College, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
# ----------------------------------------------------------------------------


# One-to-Many ----------------------------------------------------------------
class Subject(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)


class Teacher(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    subject_code = models.ForeignKey(Subject, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
# ----------------------------------------------------------------------------


# Many-to-Many ---------------------------------------------------------------
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Articles(models.Model):
    article_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    liked_users = models.ManyToManyField(User)
# ----------------------------------------------------------------------------


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
