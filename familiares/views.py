from django.shortcuts import render
from familiares.models import familiar
# Create your views here.
def familiares(request):
    familiar_1 = familiar.objects.create(
        nombre = 'Andrea',
        apellido = 'Schianchi',
        Tipo = 'Mamá',
        edad = 53,
        nacimiento = '1969-04-13'
    )
    familiar_2 = familiar.objects.create(
        nombre = 'Malena',
        apellido = 'Benitez',
        Tipo = 'Hermana',
        edad = 22,
        nacimiento = '1999-10-19'
    )
    familiar_3 = familiar.objects.create(
        nombre = 'Diego',
        apellido = 'Benitez',
        Tipo = 'Papá',
        edad = 52,
        nacimiento = '1970-07-07'
    )
    context={'familiar_1': familiar_1,'familiar_2': familiar_2, 'familiar_3': familiar_3}
    return render (request, 'familiares.html', context=context)
