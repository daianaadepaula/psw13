from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Navigators(models.Model):
  nome = models.CharField(max_length=255)
  user = models.ForeignKey(User, on_delete=models.CASCADE) # mentor
  
  def __str__(self):
    return self.nome

class Mentorados(models.Model):
  estagio_choices = (
		('E1', '10-100k'),
		('E2', '100k-1M'),
		('E3', '1M-10M'),
		('E4', '10M-100M'),		
	)
  nome = models.CharField(max_length=255)
  foto = models.ImageField(upload_to='fotos', null= True, blank=True)
  estagio = models.CharField(max_length=4, choices=estagio_choices)
  navigator = models.ForeignKey(Navigators, null=True, blank=True, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE) # mentor
  criado_em = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.nome