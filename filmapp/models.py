from django.db import models
from django.contrib.auth.models import User

class Aktyor(models.Model):
    ism=models.CharField(max_length=50)
    jins=models.CharField(max_length=20)
    tugilgan_yil=models.DateField()
    davlat=models.CharField(max_length=50)
    def __str__(self): return self.ism

class Kino(models.Model):
    nom=models.CharField(max_length=50)
    yil=models.DateField()
    reyting=models.FloatField()
    janr=models.CharField(max_length=50)
    aktyorlar=models.ManyToManyField(Aktyor)

    def __str__(self): return self.nom

class Comment(models.Model):
    matn=models.TextField()
    sana=models.DateField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    kino=models.ForeignKey(Kino, on_delete=models.CASCADE, null=True)

    def __str__(self): return self.user.username
