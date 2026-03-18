from django.http import JsonResponse
from .models import Woreda

def woredas_by_subcity(request, subcity_id):
    woredas = Woreda.objects.filter(sub_city_id=subcity_id).values('id', 'name')
    return JsonResponse(list(woredas), safe=False)
