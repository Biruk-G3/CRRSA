from django.urls import path
from .views import woredas_by_subcity

urlpatterns = [
    path('woredas/<int:subcity_id>/', woredas_by_subcity, name='woredas_by_subcity'),
]
