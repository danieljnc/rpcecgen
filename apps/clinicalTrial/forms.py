from django import forms
  
# iterable
RECRUITMENT_STATUS_CHOICES =(
    (None, " "),
    ("Pending", "Pending"),
    ("Recruiting", "Recruiting"),
    ("Suspended", "Suspended"),
    ("Complete", "Complete"),
)

PHASE_CHOICES =(
    (None, " "),
    ("N/A", "N/A"),
    ("0", "0"),
    ("1", "1"),
    ("1-2", "1-2"),
    ("2", "2"),
    ("2-3", "2-3"),
    ("3", "3"),
    ("4", "4"),
)

COVID_TRIAL_CHOICES =(
    (None, " "),
    (1, "Covid trial"),    
)
  
# creating a form 
class TrialFiltersForm(forms.Form):
    recruitment_status_field = forms.ChoiceField(choices=RECRUITMENT_STATUS_CHOICES, required=False, label='Recruitment status', widget=forms.Select(attrs={'class':'form-control'}))
    phase_field = forms.ChoiceField(choices=PHASE_CHOICES, required=False, label='Phase', widget=forms.Select(attrs={'class':'form-control'}))
    covid_trial_field = forms.ChoiceField(choices=COVID_TRIAL_CHOICES, required=False, label='Covid trial', widget=forms.Select(attrs={'class':'form-control'}))