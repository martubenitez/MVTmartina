from django.shortcuts import render
from familiares.models import familiar
# Create your views here.
def familiares(request):
    familiares = familiar.objects.all()
    context={'familiares': familiares}
    return render (request, 'familiares.html', context=context )
