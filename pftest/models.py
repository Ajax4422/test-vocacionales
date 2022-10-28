from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class ocupaciones(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('Ocupacion', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name


class materias(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('Materia', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name


class habilidades(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('Habilidad', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name


class valores(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=50)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('Valor', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name


class preguntas(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    relation = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('Pregunta', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.description

class estudiante(models.Model):
    ci = models.IntegerField(primary_key=True, default=0)
    name = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    u_educativa = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def get_absolute_url(self):
        return reverse('Estudiante', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name + " " + self.lastname


class respuestas_ocupacion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    categoria_ocupacional_1 = models.IntegerField()
    categoria_ocupacional_2 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Respuesta_ocupacion', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user


class respuestas_materia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    materia_1 = models.IntegerField()
    materia_2 = models.IntegerField()
    materia_3 = models.IntegerField()
    materia_4 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Respuesta_materia', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user


class respuestas_habilidad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    habilidad_1 = models.IntegerField()
    habilidad_2 = models.IntegerField()
    habilidad_3 = models.IntegerField()
    habilidad_4 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Respuesta_habilidad', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user


class respuestas_valor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    valor_1 = models.IntegerField()
    valor_2 = models.IntegerField()
    valor_3 = models.IntegerField()
    valor_4 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Respuesta_valor', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user


class respuestas_q1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    r4 = models.IntegerField()
    r5 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Respuesta_q1', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user


class respuestas_q2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    r4 = models.IntegerField()
    r5 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Respuesta_q2', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user


class respuestas_q3(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    r4 = models.IntegerField()
    r5 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Respuesta_q3', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user


class respuestas_q4(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    r4 = models.IntegerField()
    r5 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Respuesta_q4', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user

class respuestas_q5(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    r4 = models.IntegerField()
    r5 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Respuesta_q5', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user


class respuestas_q6(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    r1 = models.IntegerField()
    r2 = models.IntegerField()
    r3 = models.IntegerField()
    r4 = models.IntegerField()
    r5 = models.IntegerField()

    def get_absolute_url(self):
        return reverse('Respuesta_q6', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.user