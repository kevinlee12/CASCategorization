from django.contrib import admin
from .models import Coordinator, Advisor, Student
from .models import School

# Register your models here.
admin.site.register(School)
admin.site.register(Coordinator)
admin.site.register(Advisor)
admin.site.register(Student)
