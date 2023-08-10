from django.urls import path
from employee.views import EmployeeListView,EmployeeDetailView

urlpatterns = [
    path("employees/",EmployeeListView.as_view(),name="employees"),
    path('employees/<int:pk>/',EmployeeDetailView.as_view(),name='employee-detail')
]
