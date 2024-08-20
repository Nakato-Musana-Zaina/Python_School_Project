from django.contrib import admin
from .models import Students
admin.site.register(Students)
filter_horizontal = ('courses',)

# Register your models here.
