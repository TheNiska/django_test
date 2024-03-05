from django.contrib import admin
from .models import (MenuItem, MenuCategory, Logger, User,
                     College, Principal, Subject, Teacher, Articles)


# Register your models here.
admin.site.register(MenuItem)
admin.site.register(MenuCategory)
admin.site.register(Logger)
admin.site.register(User)
admin.site.register(College)
admin.site.register(Principal)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Articles)
