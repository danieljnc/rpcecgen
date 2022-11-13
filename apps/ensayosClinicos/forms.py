from django import forms
  
# iterable
ESTADO_RECLUTAMIENTO_CHOICES =(
    (None, " "),
    ("Sin iniciar reclutamiento", "Sin iniciar reclutamiento"),
    ("En reclutamiento", "En reclutamiento"),
    ("Reclutamiento detenido", "Reclutamiento detenido"),
    ("Reclutamiento cerrado", "Reclutamiento cerrado"),
)

TIPO_INTERVENCION_CHOICES =(
    (None, " "),
    ("Fármacos (incluyendo placebo)", "Fármacos (incluyendo placebo)"),
    ("Equipos médicos (incluyendo las simulaciones)", "Equipos médicos (incluyendo las simulaciones)"),
    ("Biológicos-Vacunas", "Biológicos-Vacunas"),
    ("Procedimientos-Quirúrgicos", "Procedimientos-Quirúrgicos"),
    ("Radiación", "Radiación"),
    ("Conductual (psicoterapia, estilos de vida aconsejables)", "Conductual (psicoterapia, estilos de vida aconsejables)"),
    ("Genética (incluye transferencia de genes, células madres, y ADN recombinante)", "Genética (incluye transferencia de genes, células madres, y ADN recombinante)"),
    ("Suplementos nutricionales (vitaminas, minerales)", "Suplementos nutricionales (vitaminas, minerales)"),
    ("Medicina natural y tradicional", "Medicina natural y tradicional"),
    ("Otros", "Otros"),
)

FASE_CHOICES =(
    (None, " "),
    ("N/A. No aplicable", "N/A. No aplicable"),
    ("0", "0"),
    ("1", "1"),
    ("1-2", "1-2"),
    ("2", "2"),
    ("2-3", "2-3"),
    ("3", "3"),
    ("4", "4"),
)

ENSAYOS_COVID_CHOICES =(
    (None, " "),
    (1, "Ensayos Covid"),       
)
  
# creating a form 
class EnsayosFiltrosForm(forms.Form):
    estado_reclutamiento_field = forms.ChoiceField(choices=ESTADO_RECLUTAMIENTO_CHOICES, required=False, label='Estado de reclutamiento', widget=forms.Select(attrs={'class':'form-control'}))
    tipo_intervencion_field = forms.ChoiceField(choices=TIPO_INTERVENCION_CHOICES, required=False, label='Tipo de intervención', widget=forms.Select(attrs={'class':'form-control'}))
    fase_field = forms.ChoiceField(choices=FASE_CHOICES, required=False, label='Fase', widget=forms.Select(attrs={'class':'form-control'}))
    ensayos_covid_field = forms.ChoiceField(choices=ENSAYOS_COVID_CHOICES, required=False, label='Ensayos covid', widget=forms.Select(attrs={'class':'form-control'}))