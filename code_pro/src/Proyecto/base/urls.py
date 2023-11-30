from django.urls import path
from .views import Inicio, Servicios, QuinesSomos, Contactos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", Inicio.as_view(), name="Inicio"),
    path("servicios", Servicios.as_view(), name="Servicios"),
    path("quienes_somos", QuinesSomos.as_view(), name="Quienes_somos"),
    path("contactos", Contactos.as_view(), name="Contactos"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)