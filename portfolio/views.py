from django.views.generic import DetailView, ListView, TemplateView

from .models import Artwork


class HomeView(TemplateView):
    template_name = "portfolio/home.html"


class ArtworkListView(ListView):
    model = Artwork
    template_name = "portfolio/artwork_list.html"
    context_object_name = "artworks"
    paginate_by = 24

    def get_queryset(self):
        return Artwork.objects.filter(is_published=True).order_by("sort_order", "-created_at")


class ArtworkDetailView(DetailView):
    model = Artwork
    template_name = "portfolio/artwork_detail.html"
    context_object_name = "artwork"

    def get_queryset(self):
        return Artwork.objects.filter(is_published=True)


class AboutView(TemplateView):
    template_name = "portfolio/about.html"


class ContactView(TemplateView):
    template_name = "portfolio/contact.html"
