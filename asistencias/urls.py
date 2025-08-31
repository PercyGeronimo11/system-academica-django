from django.urls import path
from .views import registrar_asistencia

urlpatterns = [
    path('registrar-asistencia/', registrar_asistencia, name='registrar_asistencia'),
]
