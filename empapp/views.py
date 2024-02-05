from django.shortcuts import render
from django.http import Http404
from .models import Employee

def employee_search(request, field, lookup, search_string):
    valid_fields = ['empname', 'empage']  # Fields that can be searched

    if field not in valid_fields or lookup not in ['startswith', 'contains', 'lte']:
        raise Http404("Invalid URL")

    if field == 'empname':
        if lookup == 'startswith':
            employees = Employee.objects.filter(fname__startswith=search_string)
        elif lookup == 'contains':
            employees = Employee.objects.filter(fname__contains=search_string)
    elif field == 'empage':
        if lookup == 'lte':
            employees = Employee.objects.filter(age__lte=search_string)

    context = {'employees': employees}
    return render(request, 'empapp/employee_list.html', context)
