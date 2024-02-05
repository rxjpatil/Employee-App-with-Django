from django.contrib import admin
from empapp.models import Employee
# Register your models here.
#admin.site.register(Product)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['empid','fname','lname','age','address']

admin.site.register(Employee,EmployeeAdmin)
