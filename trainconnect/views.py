from django.shortcuts import render, HttpResponse , get_object_or_404
import trainconnect.models as models
from random import randint

# Create your views here.
# def index(request):
#     return render(request, "trainconnect/index.html",  {

#     })
def index(request):
    return render(request, 'trainconnect/index.html', {
        "trains": models.Train.objects.all()
        
    })

#le get_object_or_404 permet d'avoir l'id de l'objet ou alors si il n'existe pas nous revoyer une erreur 404
def details(request, id):
    return render(request, 'trainconnect/details.html', {
        "train": get_object_or_404(models.Train, train_id = id)
    })

# on va chercher le nombre d'objet qu'il y a dans la db qu'on stock dans une variable puis on va faire un random int pour avoir un chiffre aléatroire entre 1 et la variable et on render l'id qu'on a eu aléatroirement
def random(request):
    ran = models.Train.objects.count()
    object_id = randint(1, ran)
    return details(request, object_id)