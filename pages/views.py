from django.shortcuts import render
from django.views.generic import TemplateView

from products.models import GeneralProduct

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = GeneralProduct.objects.filter().order_by('-total_available_in_stock')[:10]
        return context
    


def AboutPageView(request):
    return render(request, 'about.html')