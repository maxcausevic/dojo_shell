from django.shortcuts import render,redirect
from .models import Dojo, Ninja

def index(request):
    all_dojos = Dojo.objects.all()
    context = {
        'all_dojos' : all_dojos
    }
    return render(request, "index.html", context)
def dojos(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
    )
    return redirect("/")
def ninjas(request):
    if request.POST['dojo_id'] == '0':
        return redirect('/')
    else:
        dojo = Dojo.objects.get(id=request.POST['dojo_id'])
        Ninja.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            dojo = dojo
        )
        return redirect("/")
