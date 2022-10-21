from django.shortcuts import render
from appArbitro.models import arbitro
from appContrato.models import persona
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
    data = {
        'equipo' : equipos
    }

    return render(request, 'equipo.html', data)

def index(request):
    data={
        
    }
    return render(request, 'index.html', data)

