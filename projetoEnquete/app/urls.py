from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^empreendimento/listar/$', listar_empreendimento, name="listar_empreendimento"),
]