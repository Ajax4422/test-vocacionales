from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio),
    path('signin/', views.start_session),
    path('logout/', views.close_session, name='logout'),
    path('signup/', views.signup, name='registro'),
    path('reg_estudiante/', views.registro_estudiante, name='estudiante'),
    path('ocupaciones/', views.vista_ocupaciones),
    path('materias/', views.vista_materia),
    path('habilidades/', views.vista_habilidades),
    path('valores/', views.vista_valores),
    path('preguntas_1/', views.preguntas_1),
    path('preguntas_2/', views.preguntas_2),
    path('preguntas_3/', views.preguntas_3),
    path('preguntas_4/', views.preguntas_4),
    path('preguntas_5/', views.preguntas_5),
    path('preguntas_6/', views.preguntas_6),
    path('resultados/', views.resultados)
]