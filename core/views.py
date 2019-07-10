from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.base import RedirectView
from .models import Link
from .forms import ShortenerForm

# Create your views here.
class CreateShorten(CreateView):
    model = Link
    form_class = ShortenerForm
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_links'] = Link.links.total_links()
        context['total_redirects'] = Link.links.total_redirects()['redirects']
        return context

class LinkPage(DetailView):
    model = Link
    template_name = 'link.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['july'] = Link.links.dates(pk=self.kwargs['pk'])[0]['july']
        return context

class RedirectLink(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        try:
            return Link.links.decode_link(self.kwargs['code'])
        except IndexError:
            print("Error decode without data")