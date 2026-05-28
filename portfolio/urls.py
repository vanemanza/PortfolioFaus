from django.urls import path

from . import views


app_name = "portfolio"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("galeria/", views.ArtworkListView.as_view(), name="artwork_list"),
    path("galeria/<slug:slug>/", views.ArtworkDetailView.as_view(), name="artwork_detail"),
    path("cv/", views.AboutView.as_view(), name="about"),
    path("contacto/", views.ContactView.as_view(), name="contact"),
]
