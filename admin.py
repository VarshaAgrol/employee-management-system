from django.contrib import admin
from .models import Profile,Task,Attendance

# Register your models here.
from .models import Task
admin.site.register(Profile)
admin.site.register(Task)
admin.site.register(Attendance)