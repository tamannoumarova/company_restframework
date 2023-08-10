from django.urls import path
from branch.views import BranchListView,BranchDetailView

urlpatterns = [
    path("branchs/",BranchListView.as_view(),name="branchs"),
    path('branchs/<int:pk>/',BranchDetailView.as_view(),name='branch-detail')
]
