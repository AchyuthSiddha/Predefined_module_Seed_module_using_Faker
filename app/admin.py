from django.contrib import admin

# Register your models here.
from app.models import Student

class Student_db(admin.ModelAdmin):
    list_display=['sno','sname','smarks','sdob','semail','saddr','sphone']


admin.site.register(Student,Student_db)