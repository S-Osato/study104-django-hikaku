from django.views import generic

class Search(generic.TemplateView):
    template_name = 'hikaku/search.html'