import django_filters
from django import forms
from taggit.managers import TaggableManager
from taggit.forms import TagField


from studios.models import Movies


class TagFilter(django_filters.CharFilter):
    field_class = TagField

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("lookup_expr", "in")
        super().__init__(*args, **kwargs)


class MovieFilter(django_filters.FilterSet):
    genre = TagFilter(field_name="genre__name")

    class Meta:
        model = Movies
        fields = ["directors", "genre", "studio"]
