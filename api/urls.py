from django.urls import path, re_path
from api.views import BankListView, BranchByIfscView,BranchesView
urlpatterns = [
    path("get-banks/", BankListView.as_view(), name='banks-list'),
    path("get-branch-by-ifsc/<pk>/", BranchByIfscView.as_view()),
    path("get-branch-by-search/", BranchesView.as_view()),
]