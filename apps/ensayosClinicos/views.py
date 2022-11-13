from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import *
from .forms import EnsayosFiltrosForm
from apps.clinicalTrial.models import DatosInternosRpcec


# Create your views here.
class EnsayosClinicosListView(ListView):
    model = ContentTypeEnsayosClinicos
    template_name = 'ensayos_clinicos/ensayos_clinicos_list.html'
    context_object_name = 'EnsayosClinicos'

    def get_queryset(self):
        ensayos_clinicos = ContentTypeEnsayosClinicos.objects.filter(
            field_cod_reg_pub_value__icontains="RPCEC").order_by(
            '-vid')
        rpcec = DatosInternosRpcec.objects.all()[0].cod_rpcec

        i = 1
        ensayo_list = []

        estado_reclutamiento = self.request.GET.get('estado_reclutamiento_field')
        if estado_reclutamiento:
            ensayos_clinicos = ensayos_clinicos.filter(field_est_reclutamiento_value=estado_reclutamiento)

        tipo_intervencion = self.request.GET.get('tipo_intervencion_field')
        if tipo_intervencion:
            ensayos_clinicos = ensayos_clinicos.filter(field_tipo_intervencion_value=tipo_intervencion)

        fase = self.request.GET.get('fase_field')
        if fase:
            ensayos_clinicos = ensayos_clinicos.filter(field_fase_value=fase)

        ensayos_covid = self.request.GET.get('ensayos_covid_field')

        if ensayos_covid == '1':
            ensayos_clinicos = ensayos_clinicos.filter(Q(field_titulo_completo_value__icontains='COVID-19') |
                                                       Q(field_titulo_completo_value__icontains='COVID 19'))

        while i <= rpcec:
            j = i
            aux = 'RPCEC' + str(j).zfill(8)
            try:
                ensayo_clinico = ensayos_clinicos.filter(field_cod_reg_pub_value=aux)[0]
                ensayo_list.append(ensayo_clinico)
            except:
                pass
            i += 1

        return ensayo_list

    def get_context_data(self, **kwargs):
        context = super(EnsayosClinicosListView, self).get_context_data(**kwargs)
        context['form'] = EnsayosFiltrosForm(initial={
            'estado_reclutamiento_field': self.request.GET.get('estado_reclutamiento_field'),
            'tipo_intervencion_field': self.request.GET.get('tipo_intervencion_field'),
            'fase_field': self.request.GET.get('fase_field'),
            'ensayos_covid_field': self.request.GET.get('ensayos_covid_field'),
        })
        return context


class EnsayoClinicoDetailView(DetailView):
    model = ContentTypeEnsayosClinicos
    template_name = 'ensayos_clinicos/ensayos_clinicos_detail.html'
    context_object_name = 'ensayo'

    def get_context_data(self, **kwargs):
        context = super(EnsayoClinicoDetailView, self).get_context_data(**kwargs)

        context['object'].field_inst_producto_value = ContentFieldInstProducto.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid
        )[0].field_inst_producto_value

        context['object'].field_numero_reg_value = ContentFieldNumeroReg.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid
        )[0].field_numero_reg_value

        context['object'].field_fecha_registro_value = ContentFieldFechaRegistro.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid
        )[0].field_fecha_registro_value

        context['object'].field_telef_investigador_number = ContentFieldTelefInvestigador.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid)

        context['object'].field_correo_investigador = ContentFieldCorreoInvestigador.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid)

        context['object'].field_codigo_cm_value = ContentFieldCodigoCm.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid
        )[0].field_codigo_cm_value

        context['object'].field_codigo_intervencion_value = ContentFieldCodigoIntervencion.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid
        )[0].field_codigo_intervencion_value

        context['object'].field_correo_contacto_gener_email = ContentFieldCorreoContactoGener.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid)

        context['object'].field_correo_contacto_cient_email = ContentFieldCorreoContactoCient.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid)

        if context['object'].field_term_estudio_value:
            context['object'].field_term_estudio_value = str(
                context['object'].field_term_estudio_value[8:10]) + '/' + str(
                context['object'].field_term_estudio_value[5:7]) + '/' + str(
                context['object'].field_term_estudio_value[0:4])

        return context
