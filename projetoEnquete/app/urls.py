from django.conf.urls import url, include
from django.urls import path
from .views import *

urlpatterns = [
    url(r'^empreendimento/listar/$', listar_empreendimento, name="listar_empreendimento"),
    path('accounts/', include('django.contrib.auth.urls')),
]
