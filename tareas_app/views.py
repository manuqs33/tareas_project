from .models import Tarea
from django.template.response import TemplateResponse

# Create your views here.
def lista_tareas(request):
    tareas = Tarea.objects.all()
    context = {'tareas': tareas}
    return TemplateResponse(request, 'index.html', context)
