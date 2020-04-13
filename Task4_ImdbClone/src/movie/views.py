from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie


# Create your views here.
class MovieList(ListView):
    model = Movie
    # paginate_by = 2


class MovieDetail(DetailView):
    model = Movie

    # def get_object(self):
    #     object = super(MovieDetail, self).get_object()
    #     object.views_count += 1
    #     object.save()
    #     return object
    #
    # def get_context_data(self, **kwargs):
    #     context = super(MovieDetail, self).get_context_data(**kwargs)
    #     context['links'] = MovieLinks.objects.filter(movie=self.get_object())
    #     context['related_movies'] = Movie.objects.filter(
    #         category=self.get_object().category)  # .order_by['created'][0:6]
    #     return context
