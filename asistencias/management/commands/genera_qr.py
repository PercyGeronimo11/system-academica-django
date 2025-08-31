from django.core.management.base import BaseCommand
from asistencias.models import Alumno
import qrcode, os
from django.conf import settings

class Command(BaseCommand):
    help = "Genera QRs para todos los alumnos"

    def handle(self, *args, **kwargs):
        alumnos = Alumno.objects.all()
        for alumno in alumnos:
            # if alumno.qr_code:
            #     continue

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(alumno.dni)
            qr.make(fit=True)

            qr_img = qr.make_image(fill_color="black", back_color="white")

            file_name = f"qrcodes/qr_{alumno.dni}.png"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            qr_img.save(file_path)

            # alumno.qr_code = file_name
            # alumno.save(update_fields=["qr_code"])

        self.stdout.write(self.style.SUCCESS("✅ QRs generados correctamente"))




# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config_app.settings")
# django.setup()

# from asistencias.models import Alumno
# import qrcode
# from django.conf import settings
# import os


# def generar_qrs_alumnos():
#     alumnos = Alumno.objects.all()
#     for alumno in alumnos:
#         # Generar QR con el DNI como contenido
#         qr_img = qrcode.make(alumno.dni)
        
#         # Nombre del archivo
#         file_name = f"qrcodes/qr_{alumno.dni}.png"
#         file_path = os.path.join(settings.MEDIA_ROOT, file_name)

#         # Guardar la imagen físicamente
#         os.makedirs(os.path.dirname(file_path), exist_ok=True)
#         qr_img.save(file_path)

#         # Guardar la ruta en la BD
#         # alumno.qr_code = file_name  # "qrcodes/qr_12345678.png"
#         # alumno.save(update_fields=["qr_code"])

#     print("✅ QRs generados y guardados correctamente.")
