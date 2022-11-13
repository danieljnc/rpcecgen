"""rpcecgen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.generator.views import generate_xml_with_template
from apps.clinicalTrial.views import *
from apps.reports.views import StatusRpcecPdf
from apps.ensayosClinicos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('clinical-trial/list', ClinicalTrialListView.as_view(), name='clinical_trial_list'),
    path('clinical-trial/detail/<int:pk>', ClinicalTrialDetailView.as_view(), name='clinical_trial_detail'),
    path('xml/template', generate_xml_with_template, name='generate_xml'),
    path('reports/status-rpcec', StatusRpcecPdf.as_view(), name='status_rpcec'),
    path('ensayo-clinico/list', EnsayosClinicosListView.as_view(), name='ensayo_clinico_list'),
    path('ensayo-clinico/detail/<int:pk>',  EnsayoClinicoDetailView.as_view(), name='ensayo_clinico_detail'),
]
