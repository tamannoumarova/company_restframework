from django.urls import path
from profession.views import ProfessionListView,ProfessionDetailView

urlpatterns = [
    path("professions/",ProfessionListView.as_view(),name="professions"),
    path('professions/<int:pk>/',ProfessionDetailView.as_view(),name='profession-detail')
]
