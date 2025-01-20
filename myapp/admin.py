from django.contrib import admin
from .models import UserData,Chart,Course,Concept

# Register your models here.
admin.site.register(UserData)
admin.site.register(Chart)
admin.site.register(Course)
admin.site.register(Concept)