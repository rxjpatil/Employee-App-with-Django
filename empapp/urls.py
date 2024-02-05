from django.urls import path
from .views import employee_search

urlpatterns = [
    path('<str:field>/<str:lookup>/<str:search_string>/', employee_search, name='employee_search'),
]
