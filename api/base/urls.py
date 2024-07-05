from django.urls import path

from api.base.views.about import AboutCompanyListView

urlpatterns = [
    path("about", AboutCompanyListView.as_view(), name="about"), ]
