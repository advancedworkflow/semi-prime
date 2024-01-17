from django.shortcuts import render
from django.template import loader
from .forms import PrimeForm
# Create your views here.

from .util import sm
import time





def home(request):
    form = PrimeForm(request.POST)
    number = 0
    error = 'le nombre est premier '
    context = {'form': form}
    if form.is_valid():
        print(f'valid{request.POST["nombre"]}')
        r = sm(int(request.POST["nombre"]))
        print(r)
        if isinstance(r,str) == False :
            context['result1'] = r[0]
            context['result2'] = r[1]
            context['weight'] = len(r[0])
        else:
            context['result1'] = r


        print(type(r), r)
        return render(request, 'home.html', context)
    else:

        return render(request, 'home.html', context)