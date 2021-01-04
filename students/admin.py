from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('s_name', 's_major', 's_age', 's_grade', 's_gender')
    list_filter = ['s_age']


admin.site.register(Student, StudentAdmin)