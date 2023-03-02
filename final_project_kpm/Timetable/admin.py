from django.contrib import admin
from.models import Student,Course,Subject,Assignment

# Register your models here.
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Assignment)