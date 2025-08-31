from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Alumno, Asistencia
from django.utils import timezone

@api_view(['POST'])
def registrar_asistencia(request):
    qr_code = request.data.get('qr_code')
    if not qr_code:
        return Response({"error": "Se requiere qr_code"}, status=400)

    try:
        alumno = Alumno.objects.get(qr_code=qr_code)
        asistencia = Asistencia.objects.create(
            alumno=alumno,
            fecha=timezone.now().date(),
            hora=timezone.now().time()
        )
        return Response({"mensaje": f"Asistencia registrada para {alumno.nombre}"})
    except Alumno.DoesNotExist:
        return Response({"error": "QR no válido"}, status=400)


