from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.BaseView.as_view(), name = "base"),
    path('new_search', views.SearchView, name = "new_search")
]
