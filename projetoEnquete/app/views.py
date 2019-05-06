from django.shortcuts import render
from .model.Empreendimento import *

def listar_empreendimento(request, template_name="empreendimento_list.html"):
    empreendimento = Empreedimento.objects.all()
    empreendimentos = {'lista': empreendimento}
    return render(request, template_name, empreendimentos)
