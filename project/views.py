from calendar import c
from django.shortcuts import render
from appArbitro.models import arbitro
from appContrato.models import contrato, persona, tipo_persona
from appEquipo.models import equipo
from user.models import User
# Create your views here.

def contadoresAdmin(request):
    arbitros = arbitro.objects.count()
    entrenadores = persona.objects.filter(tipo_persona_id=2).count()
    jugadores = persona.objects.filter(tipo_persona_id=1).count()
    equipos = equipo.objects.count()
    usuarios = User.objects.all()
    data = {
        'arbitros' : arbitros,
        'entrenadores' : entrenadores,
        'jugadores' : jugadores,
        'equipos' : equipos,
        'usuarios': usuarios
    }
    return render(request, 'admin/index.html', data)

def contextoJugador(request):

    data = {
        
    }

    return render(request, 'jugador.html', data)

def contextoEquipo(request, nombre_equipo):
    equipos = equipo.objects.get(nombre=nombre_equipo.upper())
    tipo_persona_entrenador = tipo_persona.objects.get(descripcion='ENTRENADOR')
    persona_entrenador = persona.objects.filter(tipo_persona_id=tipo_persona_entrenador.tipo_persona_id)
    listaentrenador = []
    for p_e in persona_entrenador:
        contratos = contrato.objects.filter(persona_id= p_e.persona_id,nuevo_club=equipos.equipo_id, estado=True)
        for c in contratos:
            if(c.estado == True):
                listaentrenador.append(c)

    data = {
        'equipo' : equipos,
        'contrato' : contratos,
        'entrenador': listaentrenador,
    }

    return render(request, 'equipo.html', data)

def index(request):
    data={
        
    }
    return render(request, 'index.html', data)
