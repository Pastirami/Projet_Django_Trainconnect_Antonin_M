from django.db import models



# Create your models here.

#Partie a pofiner plus tard(pour appliquer directement l'api sncf que l'on puisse mettre des trains reel sur le site.)
# class Gare(models.Model):
#     gare_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30)
#     latitude = models.FloatField()
#     longitude = models.FloatField()

#Ma classe Train qui me permet de géneré mes trains de definir la gare de départ d'arrivé si le train est en retard annulé ou a l'heure.
class Train(models.Model):
    class Status(models.IntegerChoices):
        ON_TIME = 1
        DELAYED = 2
        CANCELLED = 3

    train_id = models.AutoField(primary_key=True)
    # gare_depart = models.ForeignKey(models.Gare, on_delete=models.CASCADE, related_name='depart')
    # gare_arrivee = models.ForeignKey(models.Gare, on_delete=models.CASCADE, related_name='arrivee')

    heure_depart = models.DateTimeField()
    heure_arrivee = models.DateTimeField()

    destination = models.CharField(max_length=30)
    status = models.IntegerField(choices=Status.choices, default=Status.ON_TIME)

    image = models.CharField(max_length=255)

