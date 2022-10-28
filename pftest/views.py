from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from .models import ocupaciones, habilidades, valores, materias
from .models import estudiante, respuestas_ocupacion, respuestas_materia, respuestas_habilidad, respuestas_valor, respuestas_q1, respuestas_q2, respuestas_q3, respuestas_q4, respuestas_q5, respuestas_q6
from .forms import forms_ocupa, forms_estudiante, forms_materia, forms_habilidad, forms_valor, forms_pregunta_1, forms_pregunta_2, forms_pregunta_3, forms_pregunta_4, forms_pregunta_5, forms_pregunta_6
from .dic_datos import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required



def Inicio(request):
    return render(request, "Inicio.html")


def signup(request):
    form = UserCreationForm()
    form.fields['username'].label = 'Nombre de usuario'
    form.fields['password1'].label = 'Contraseña'
    form.fields['password2'].label = 'Confirmar contraseña'
    form.fields['username'].help_text = 'Requiere 150 caracteres o menos. Letras, numeros y @/./+/-/_ solamente.'
    form.fields['password1'].help_text = "<ul class='list-group'><li class='list-group-item list-group-item-secondary'>Tu contraseña no puede ser muy similar a tus otros datos personales.</li> <li class='list-group-item list-group-item-success'>Tu contraseña debe contener al menos 8 caracteres.</li> <li class='list-group-item list-group-item-warning'>Tu contraseña no puede ser una contraseña comun.</li> <li class='list-group-item list-group-item-danger'>Tu contraseña no puede ser completamente numerica.</li></ul>"
    form.fields['password2'].help_text = 'Ingresa la misma contraseña que antes, para verificacion.'
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('../reg_estudiante/')
            except:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'form': form, 'error': 'El usuario ya existe'})
    else:
        return render(request, "signup.html", {
        'form': form
    })

@login_required
def close_session(request):
    logout(request)
    return redirect('../')


def start_session(request):
    form = AuthenticationForm()
    form.fields['username'].label = 'Nombre de usuario'
    form.fields['password'].label = 'Contraseña'
    if request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('../')
        else:
            return render(request, 'signin.html', {'form': form, 'error': 'El usuario o la contraseña son incorrectos'})
    else:
        return render(request, "signin.html", {
            'form': form
            })

@login_required
def registro_estudiante(request):
    if request.method == "POST":
        try:
            print(request.POST)
            est = estudiante(ci = request.POST['CI'],
                                name = request.POST['nombre'],
                                lastname = request.POST['apellido'],
                                age = request.POST['edad'],
                                email = request.POST['email'],
                                u_educativa = request.POST['unidad_educativa'],
                                user = request.user)
            est.save()
            return redirect('../')
        except:
            return render(request, "estudiante.html", {
                'form': form,
                'error': 'El usuario ya existe'
            })
    else:
        form = forms_estudiante()
    return render(request, "estudiante.html", {
        'form': form
    })

@login_required
def vista_ocupaciones(request):
    if request.method == "POST":
        if request.POST['categoria_ocupacional_1'] ==  request.POST['categoria_ocupacional_2']:
            ocu = ocupaciones.objects.all()
            form = forms_ocupa()
            return render(request, "ocupaciones.html", {
                'oc': ocu,
                'form': form,
                'error': 'Las categorias ocupacionales no pueden ser iguales'
            })
        else:
            try:
                ocupa = respuestas_ocupacion(user = request.user,
                                                categoria_ocupacional_1 = int(request.POST['categoria_ocupacional_1']),
                                                categoria_ocupacional_2 = int(request.POST['categoria_ocupacional_2']))
                ocupa.save()
                return redirect('../materias/')
            except:
                ocu = ocupaciones.objects.all()
                form = forms_ocupa()
                return render(request, "ocupaciones.html", {
                        'oc': ocu,
                        'form': form,
                        'error': 'El usuario ya existe'
                        })
    else:
        ocu = ocupaciones.objects.all()
        form = forms_ocupa()
        return render(request, "ocupaciones.html", {
            'oc': ocu,
            'form': form
        })

@login_required
def vista_materia(request):
    if request.method == "POST":
        if (request.POST['materia_1'] ==  request.POST['materia_2']) or (request.POST['materia_1'] ==  request.POST['materia_3']) or (request.POST['materia_1'] ==  request.POST['materia_4']) or  (request.POST['materia_2'] ==  request.POST['materia_3']) or  (request.POST['materia_2'] ==  request.POST['materia_4']) or  (request.POST['materia_3'] ==  request.POST['materia_4']):
            mate = materias.objects.all()
            form = forms_materia()
            return render(request, "materias.html", {
                'mat': mate,
                'form': form,
                'error': 'Las materias no pueden ser iguales'
            })
        else:
            try:
                mat = respuestas_materia(user = request.user,
                                materia_1 = int(request.POST['materia_1']),
                                materia_2 = int(request.POST['materia_2']),
                                materia_3 = int(request.POST['materia_3']),
                                materia_4 = int(request.POST['materia_4']))
                mat.save()
                return redirect('../habilidades/')
            except:
                mate = materias.objects.all()
                form = forms_materia()
                return render(request, "materias.html", {
                    'mat': mate,
                    'form': form,
                    'error': 'El usuario ya existe'
                })
    else:
        mate = materias.objects.all()
        form = forms_materia()
        return render(request, "materias.html", {
            'mat': mate,
            'form': form
        })

@login_required
def vista_habilidades(request):
    if request.method == "POST":
        if (request.POST['habilidad_1'] ==  request.POST['habilidad_2']) or (request.POST['habilidad_1'] ==  request.POST['habilidad_3']) or (request.POST['habilidad_1'] ==  request.POST['habilidad_4']) or  request.POST['habilidad_2'] ==  request.POST['habilidad_3'] or  request.POST['habilidad_2'] ==  request.POST['habilidad_4'] or  request.POST['habilidad_3'] ==  request.POST['habilidad_4']:
            habl = habilidades.objects.all()
            form = forms_habilidad()
            return render(request, "habilidades.html", {
                'hab': habl,
                'form': form,
                'error': 'Las habilidades no pueden ser iguales'
            })
        else:
            try:
                hab = respuestas_habilidad(user = request.user,
                                habilidad_1 = int(request.POST['habilidad_1']),
                                habilidad_2 = int(request.POST['habilidad_2']),
                                habilidad_3 = int(request.POST['habilidad_3']),
                                habilidad_4 = int(request.POST['habilidad_4']))
                hab.save()
                return redirect('../valores/')
            except:
                habl = habilidades.objects.all()
                form = forms_habilidad()
                return render(request, "habilidades.html", {
                    'hab': habl,
                    'form': form,
                    'error': 'El usuario ya existe'
                })
    else:
        habl = habilidades.objects.all()
        form = forms_habilidad()
        return render(request, "habilidades.html",{
            'hab': habl,
            'form': form
        })

@login_required
def vista_valores(request):
    if request.method == "POST":
        if (request.POST['valor_1'] ==  request.POST['valor_2']) or (request.POST['valor_1'] ==  request.POST['valor_3']) or (request.POST['valor_1'] ==  request.POST['valor_4']) or  (request.POST['valor_2'] ==  request.POST['valor_3']) or  (request.POST['valor_2'] ==  request.POST['valor_4']) or  (request.POST['valor_3'] ==  request.POST['valor_4']):
            valo = valores.objects.all()
            form = forms_valor()
            return render(request, "valores.html", {
                'val': val,
                'form': form,
                'error': 'Los valores no pueden ser iguales'
            })
        else:
            try:
                val = respuestas_valor(user = request.user,
                                    valor_1 = int(request.POST['valor_1']),
                                    valor_2 = int(request.POST['valor_2']),
                                    valor_3 = int(request.POST['valor_3']),
                                    valor_4 = int(request.POST['valor_4']))
                val.save()
                return redirect('../preguntas_1/')
            except:
                valo = valores.objects.all()
                form = forms_valor()
                return render(request, "valores.html", {
                        'val': valo,
                        'form': form,
                        'error': 'El usuario ya existe'
                    })
    else:
        valo = valores.objects.all()
        form = forms_valor()
        return render(request, "valores.html", {
            'val': valo,
            'form': form
    })

@login_required
def preguntas_1(request):
    if request.method == "POST":
        try:
            preg = respuestas_q1(user = request.user,
                            r1 = int(request.POST['pregunta_1']),
                            r2 = int(request.POST['pregunta_2']),
                            r3 = int(request.POST['pregunta_3']),
                            r4 = int(request.POST['pregunta_4']),
                            r5 = int(request.POST['pregunta_5']))
            preg.save()
            return redirect('../preguntas_2/')
        except:
            return render(request, "preguntas_1.html", {
                'error': 'no registro respuesta'
            })
    else:
        q1 = intereses[1][0]
        q2 = intereses[2][0]
        q3 = intereses[3][0]
        q4 = intereses[4][0]
        q5 = intereses[5][0]
        form  = forms_pregunta_1()
        return render(request, "preguntas_1.html", {
            'q1': q1,
            'q2': q2,
            'q3': q3,
            'q4': q4,
            'q5': q5,
            'form': form
        })

@login_required
def preguntas_2(request):
    if request.method == "POST":
        try:
            preg = respuestas_q2(user = request.user,
                            r1 = int(request.POST['pregunta_6']),
                            r2 = int(request.POST['pregunta_7']),
                            r3 = int(request.POST['pregunta_8']),
                            r4 = int(request.POST['pregunta_9']),
                            r5 = int(request.POST['pregunta_10']))
            preg.save()
            return redirect('../preguntas_3/')
        except:
            return render(request, "preguntas_2.html", {
                'error': 'no registro respuesta'
            })
    else:
        q1 = intereses[6][0]
        q2 = intereses[7][0]
        q3 = intereses[8][0]
        q4 = intereses[9][0]
        q5 = intereses[10][0]
        form  = forms_pregunta_2()
        return render(request, "preguntas_2.html", {
            'q1': q1,
            'q2': q2,
            'q3': q3,
            'q4': q4,
            'q5': q5,
            'form': form
        })

@login_required
def preguntas_3(request):
    if request.method == "POST":
        try:
            preg = respuestas_q3(user = request.user,
                            r1 = int(request.POST['pregunta_11']),
                            r2 = int(request.POST['pregunta_12']),
                            r3 = int(request.POST['pregunta_13']),
                            r4 = int(request.POST['pregunta_14']),
                            r5 = int(request.POST['pregunta_15']))
            preg.save()
            return redirect('../preguntas_4/')
        except:
            return render(request, "preguntas_3.html", {
                'error': 'no registro respuesta'
            })
    else:
        q1 = intereses[11][0]
        q2 = intereses[12][0]
        q3 = intereses[13][0]
        q4 = intereses[14][0]
        q5 = intereses[15][0]
        form  = forms_pregunta_3()
        return render(request, "preguntas_3.html", {
            'q1': q1,
            'q2': q2,
            'q3': q3,
            'q4': q4,
            'q5': q5,
            'form': form
        })

@login_required
def preguntas_4(request):
    if request.method == "POST":
        try:
            preg = respuestas_q4(user = request.user,
                            r1 = int(request.POST['pregunta_16']),
                            r2 = int(request.POST['pregunta_17']),
                            r3 = int(request.POST['pregunta_18']),
                            r4 = int(request.POST['pregunta_19']),
                            r5 = int(request.POST['pregunta_20']))
            preg.save()
            return redirect('../preguntas_5/')
        except:
            return render(request, "preguntas_4.html", {
                'error': 'no registro respuesta'
            })
    else:
        q1 = intereses[16][0]
        q2 = intereses[17][0]
        q3 = intereses[18][0]
        q4 = intereses[19][0]
        q5 = intereses[20][0]
        form  = forms_pregunta_4()
        return render(request, "preguntas_4.html", {
            'q1': q1,
            'q2': q2,
            'q3': q3,
            'q4': q4,
            'q5': q5,
            'form': form
        })

@login_required
def preguntas_5(request):
    if request.method == "POST":
        try:
            preg = respuestas_q5(user = request.user,
                            r1 = int(request.POST['pregunta_21']),
                            r2 = int(request.POST['pregunta_22']),
                            r3 = int(request.POST['pregunta_23']),
                            r4 = int(request.POST['pregunta_24']),
                            r5 = int(request.POST['pregunta_25']))
            preg.save()
            return redirect('../preguntas_6/')
        except:
            return render(request, "preguntas_5.html", {
                'error': 'no registro respuesta'
            })
    else:
        q1 = intereses[21][0]
        q2 = intereses[22][0]
        q3 = intereses[23][0]
        q4 = intereses[24][0]
        q5 = intereses[25][0]
        form  = forms_pregunta_5()
        return render(request, "preguntas_5.html", {
            'q1': q1,
            'q2': q2,
            'q3': q3,
            'q4': q4,
            'q5': q5,
            'form': form
        })

@login_required
def preguntas_6(request):
    if request.method == "POST":
        try:
            preg = respuestas_q6(user = request.user,
                            r1 = int(request.POST['pregunta_26']),
                            r2 = int(request.POST['pregunta_27']),
                            r3 = int(request.POST['pregunta_28']),
                            r4 = int(request.POST['pregunta_29']),
                            r5 = int(request.POST['pregunta_30']))
            preg.save()
            return redirect('../resultados/')
        except:
            form  = forms_pregunta_6()
            return render(request, "preguntas_6.html", {
                'error': 'no registro respuesta'
            })
    else:
        q1 = intereses[26][0]
        q2 = intereses[27][0]
        q3 = intereses[28][0]
        q4 = intereses[29][0]
        q5 = intereses[30][0]
        form  = forms_pregunta_6()
        return render(request, "preguntas_6.html", {
            'q1': q1,
            'q2': q2,
            'q3': q3,
            'q4': q4,
            'q5': q5,
            'form': form
        })

@login_required
def resultados(request):
    estu = estudiante.objects.filter(user = request.user).values()
    nom_est = estu[0]['name'] + " "+ estu[0]['lastname']
    ocu = respuestas_ocupacion.objects.filter(user = request.user).latest('id')
    q1 = respuestas_q1.objects.filter(user = request.user).latest('id')
    q2 = respuestas_q2.objects.filter(user = request.user).latest('id')
    q3 = respuestas_q3.objects.filter(user = request.user).latest('id')
    q4 = respuestas_q4.objects.filter(user = request.user).latest('id')
    q5 = respuestas_q5.objects.filter(user = request.user).latest('id')
    q6 = respuestas_q6.objects.filter(user = request.user).latest('id')
    personalidades = relaciones([q1.__dict__, q2.__dict__, q3.__dict__, q4.__dict__, q5.__dict__, q6.__dict__])
    personalidades = dict(sorted(personalidades.items(), key=lambda item: item[1], reverse=True))
    keys_res = list(personalidades.keys())
    cor_1 = keys_res[0]+keys_res[1]
    lis_cor1, indice_cor1 = correlacion(cor_1)
    cor_2 = keys_res[0]+keys_res[2]
    lis_cor2 = correlacion2(cor_2, indice_cor1)
    puntaje_1 = personalidades[keys_res[0]]
    nombre_personalidad_1 = tiposO_dic[keys_res[0]][0]
    descripcion_personalidad_1 = tiposO_dic[keys_res[0]][1]
    puntaje_2 = personalidades[keys_res[1]]
    nombre_personalidad_2 = tiposO_dic[keys_res[1]][0]
    descripcion_personalidad_2 = tiposO_dic[keys_res[1]][1]
    puntaje_3 = personalidades[keys_res[2]]
    nombre_personalidad_3 = tiposO_dic[keys_res[2]][0]
    descripcion_personalidad_3 = tiposO_dic[keys_res[2]][1]
    return render(request, 'resultados.html', {
        'estudiante': nom_est,
        'puntaje_1': puntaje_1,
        "nombre_personalidad_1": nombre_personalidad_1,
        'descripcion_personalidad_1': descripcion_personalidad_1,
        'puntaje_2': puntaje_2,
        'nombre_personalidad_2': nombre_personalidad_2,
        'descripcion_personalidad_2': descripcion_personalidad_2,
        'puntaje_3': puntaje_3,
        'nombre_personalidad_3': nombre_personalidad_3,
        'descripcion_personalidad_3': descripcion_personalidad_3,
        'lista_correlacion_1': lis_cor1,
        'lista_correlacion_2': lis_cor2,
    })


def relaciones(list_res):
    R = 0
    C = 0
    A = 0
    S = 0
    E = 0
    O = 0
    con = 1
    for q in list_res:
        for keys, values in q.items():
            if (keys == 'r1') or (keys == 'r2') or (keys == 'r3') or (keys == 'r4') or (keys == 'r5'):
                if intereses[con][1] == 'R':
                    R += int(values)
                elif intereses[con][1] == 'C':
                    C += int(values)
                elif intereses[con][1] == 'A':
                    A += int(values)
                elif intereses[con][1] == 'S':
                    S += int(values)
                elif intereses[con][1] == 'E':
                    E += int(values)
                elif intereses[con][1] == 'O':
                    O += int(values)
                con += 1
    return {'R': R, 'C': C, 'A': A, 'S': S, 'E': E, 'O': O}


def correlacion(corr1):
    ocupaciones1 = cor_dic[corr1]
    lista_correlacion = []
    lista_indice = []
    for values in ocupaciones1.values():
        oc = ocupacion_dic[values]
        mat_corr1, habl_corr1, val_corr1 = elementos_correlacion(values, lista_indice)
        lista_correlacion.append({'nombre': oc[0], 'descripcion': oc[1], 'lista_materia': mat_corr1, 'lista_habilidad': habl_corr1, 'lista_valor': val_corr1})
        lista_indice.append(values)
    return lista_correlacion, lista_indice


def correlacion2(corr1, lista_indice):
    ocupaciones1 = cor_dic[corr1]
    lista_correlacion = []
    for values in ocupaciones1.values():
        oc = ocupacion_dic[values]
        if values not in lista_indice:
            mat_corr1, habl_corr1, val_corr1 = elementos_correlacion(values, lista_indice)
            lista_correlacion.append({'nombre': oc[0], 'descripcion': oc[1], 'lista_materia': mat_corr1, 'lista_habilidad': habl_corr1, 'lista_valor': val_corr1})
    return lista_correlacion


def elementos_correlacion(corr_indice, lista_indice):
    lista_materias_corr = []
    lista_habilidades_corr = []
    lista_valores_corr = []
    tabla_corr = tr_dic[corr_indice]
    if corr_indice not in lista_indice:
        for materias in tabla_corr[0]:
            lista_materias_corr.append({'materia': materia_dic[materias][0], 'descripcion': materia_dic[materias][1]})
        for habilidades in tabla_corr[1]:
            lista_habilidades_corr.append({'habilidad': habilidad_dic[habilidades][0], 'descripcion': habilidad_dic[habilidades][1]})
        for valores in tabla_corr[2]:
            lista_valores_corr.append({'valor': valor_dic[valores][0], 'descripcion': valor_dic[valores][1]})
        return lista_materias_corr, lista_habilidades_corr, lista_valores_corr
    else:
        return lista_materias_corr, lista_habilidades_corr, lista_valores_corr
