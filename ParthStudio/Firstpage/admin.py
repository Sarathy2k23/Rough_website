from django.contrib import admin
from Firstpage.models import Student

# Register your models here.
class Student_bio(admin.ModelAdmin):
    Student_detail=['first_name','last_name']
    
admin.site.register(Student,Student_bio)
