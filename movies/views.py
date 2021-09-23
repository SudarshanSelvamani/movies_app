from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.urls import reverse_lazy, reverse
from django.contrib import messages


from studios.models import Movies
from .forms import MovieCreateForm
from .filters import MovieFilter


class MovieListView(ListView):
    model = Movies
    paginate_by = 6
    context_object_name = "movies"
    template_name = "movies/movie_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = MovieFilter(self.request.GET, queryset=self.get_queryset())
        return context


class MovieCreateView(CreateView):
    form_class = MovieCreateForm
    template_name = "movies/create_movie.html"
    success_url = reverse_lazy("movies:list")


class MovieUpdateView(UpdateView):
    model = Movies
    form_class = MovieCreateForm
    template_name = "movies/create_movie.html"
    success_url = reverse_lazy("movies:list")


class MovieDeleteView(DeleteView):
    model = Movies
    template_name = "movies/delete_movie.html"
    context_object_name = "movie"

    def get_success_url(self):
        messages.success(self.request, "movie was deleted successfully.")
        return reverse("movies:list")


class MovieDetailView(DetailView):
    model = Movies
    template_name = "movies/detail_view.html"
    context_object_name = "movie"
