from django.contrib import admin
from .models import User
# Register your models here.
from .models import student
# Register your models here.
admin.site.register(student)

admin.site.register(User)