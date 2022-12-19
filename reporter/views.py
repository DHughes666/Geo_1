from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.serializers import serialize
from .models import Incidence, Airport

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'reporter/index.html'


"""
def airport_datasets(request):
    air = Airport.objects.all()
    serializer = AirportSerializer(air, many=True)
    return HttpResponse(serializer.data, content_type='json')
"""


def airport_dataset(request):
    airports = serialize('geojson', Airport.objects.all())
    return HttpResponse(airports, content_type='json')
