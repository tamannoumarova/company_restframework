from django.urls import path
from department.views import DepartmentListView,DepartmentDetailView

urlpatterns = [
    path("departments/",DepartmentListView.as_view(),name="departments"),
    path('departments/<int:pk>/',DepartmentDetailView.as_view(),name='department-detail')
]
