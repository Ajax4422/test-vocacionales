from django.contrib import admin

# Register your models here.
from pftest.models import ocupaciones, materias, habilidades, valores, preguntas
from pftest.models import estudiante, respuestas_ocupacion, respuestas_materia, respuestas_habilidad, respuestas_valor
from pftest.models import respuestas_q1, respuestas_q2, respuestas_q3, respuestas_q4, respuestas_q5, respuestas_q6

admin.site.register(ocupaciones)
admin.site.register(materias)
admin.site.register(habilidades)
admin.site.register(valores)
admin.site.register(preguntas)
admin.site.register(estudiante)
admin.site.register(respuestas_ocupacion)
admin.site.register(respuestas_materia)
admin.site.register(respuestas_habilidad)
admin.site.register(respuestas_valor)
admin.site.register(respuestas_q1)
admin.site.register(respuestas_q2)
admin.site.register(respuestas_q3)
admin.site.register(respuestas_q4)
admin.site.register(respuestas_q5)
admin.site.register(respuestas_q6)





