from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class forms_estudiante(forms.Form):
    CI = forms.IntegerField(required=True, label="CI:", widget=forms.widgets.NumberInput(
            attrs={
                "class": "form-control"
            }))
    nombre = forms.CharField(max_length=100, required=True, label="Nombre(s):", widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Ej. Juan Manuel",
                "class": "form-control"
            }))
    apellido = forms.CharField(max_length=100, required=True, label="Apellidos:", widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "E.j. Lopez Perez",
                "class": "form-control"
            }))
    edad = forms.IntegerField(required=True, label="Edad:", widget=forms.widgets.NumberInput(
            attrs={
                "class": "form-control"
            }))
    email = forms.CharField(max_length=100, required=True, label="E-mail:", widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "correo@correo.com",
                "class": "form-control"
            }))
    unidad_educativa = forms.CharField(max_length=150, required=True, label="Unidad Educativa:", widget=forms.widgets.TextInput(
            attrs={
                "placeholder": "Ej. Puerto de Mejillones",
                "class": "form-control"
            }))


class forms_ocupa(forms.Form):
    categoria_ocupacional_1 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(14),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "14",
                "placeholder": "1 - 14",
                "class": "form-control"
            }))
    categoria_ocupacional_2 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(14),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "14",
                "placeholder": "1 - 14",
                "class": "form-control"
            }))


class forms_materia(forms.Form):
    materia_1 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(16),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "16",
                "placeholder": "1 - 16",
                "class": "form-control"
            }))
    materia_2 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(16),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "16",
                "placeholder": "1 - 16",
                "class": "form-control"
            }))
    materia_3 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(16),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "16",
                "placeholder": "1 - 16",
                "class": "form-control"
            }))
    materia_4 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(16),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "16",
                "placeholder": "1 - 16",
                "class": "form-control"
            }))


class forms_habilidad(forms.Form):
    habilidad_1 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(16),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "16",
                "placeholder": "1 - 16",
                "class": "form-control"
            }))
    habilidad_2 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(16),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "16",
                "placeholder": "1 - 16",
                "class": "form-control"
            }))
    habilidad_3 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(16),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "16",
                "placeholder": "1 - 16",
                "class": "form-control"
            }))
    habilidad_4 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(16),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "16",
                "placeholder": "1 - 16",
                "class": "form-control"
            }))

class forms_valor(forms.Form):
    valor_1 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "12",
                "placeholder": "1 - 12",
                "class": "form-control"
            }))
    valor_2 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "12",
                "placeholder": "1 - 12",
                "class": "form-control"
            }))
    valor_3 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "12",
                "placeholder": "1 - 12",
                "class": "form-control"
            }))
    valor_4 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "1",
                "max": "12",
                "placeholder": "1 - 12",
                "class": "form-control"
            }))


class forms_pregunta_1(forms.Form):
    pregunta_1 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_2 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_3 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_4 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_5 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))


class forms_pregunta_2(forms.Form):
    pregunta_6 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_7 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_8 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_9 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_10 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))


class forms_pregunta_3(forms.Form):
    pregunta_11 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_12 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_13 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_14 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_15 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))


class forms_pregunta_4(forms.Form):
    pregunta_16 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_17 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_18 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_19 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_20 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))


class forms_pregunta_5(forms.Form):
    pregunta_21 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_22 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_23 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_24 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_25 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))


class forms_pregunta_6(forms.Form):
    pregunta_26 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_27 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_28 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_29 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))
    pregunta_30 = forms.IntegerField(required=True, validators=[
            MaxValueValidator(3),
            MinValueValidator(0)
        ], widget=forms.widgets.NumberInput(
            attrs={
                "min": "0",
                "max": "3",
                "placeholder": "0 - 3",
                "class": "form-control"
            }))