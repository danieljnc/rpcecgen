from django.db import models


# Create your models here.
class ContentTypeEnsayosClinicos(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    field_sigla_abreviado_value = models.TextField(blank=True, null=True)
    field_titulo_completo_value = models.TextField(blank=True, null=True)
    field_siglas_value = models.TextField(blank=True, null=True)
    field_palabras_value = models.TextField(blank=True, null=True)
    field_promotor_value = models.TextField(blank=True, null=True)
    field_part_cencec_value = models.TextField(blank=True, null=True)
    field_fuente_fin_value = models.TextField(blank=True, null=True)
    field_instancia_reg_value = models.TextField(blank=True, null=True)
    field_inst_reguladoras_value = models.TextField(blank=True, null=True)
    field_otra_instancias_value = models.TextField(blank=True, null=True)
    field_fecha_notific_value = models.DateTimeField(blank=True, null=True)
    field_fecha_autoriz_value = models.DateTimeField(blank=True, null=True)
    field_numero_ref_value = models.TextField(blank=True, null=True)
    field_estadop_value = models.TextField(blank=True, null=True)
    field_1er_investigador_value = models.TextField(blank=True, null=True)
    field_2do_investigador_value = models.TextField(blank=True, null=True)
    field_apellidos_investigador_value = models.TextField(blank=True, null=True)
    field_esp_investigador_value = models.TextField(blank=True, null=True)
    field_trab_investigador_value = models.TextField(blank=True, null=True)
    field_dir_investigador_value = models.TextField(blank=True, null=True)
    field_prov_investigador_value = models.TextField(blank=True, null=True)
    field_pais_investigador_value = models.TextField(blank=True, null=True)
    field_cod_investigador_value = models.TextField(blank=True, null=True)
    field_est_ensayo_value = models.TextField(blank=True, null=True)
    field_causa_ter_value = models.TextField(blank=True, null=True)
    field_est_reclutamiento_value = models.TextField(blank=True, null=True)
    field_fecha_1er_incluido_value = models.DateTimeField(blank=True, null=True)
    field_fecha_ult_incluido_value = models.DateTimeField(blank=True, null=True)
    field_total_paciente_value = models.TextField(blank=True, null=True)
    field_cond_medica_value = models.TextField(blank=True, null=True)
    field_palabras_cm_value = models.TextField(blank=True, null=True)
    field_tipo_intervencion_value = models.TextField(blank=True, null=True)
    field_breve_value = models.TextField(blank=True, null=True)
    field_palabras_intervencion_value = models.TextField(blank=True, null=True)
    field_totalg_value = models.TextField(blank=True, null=True)
    field_obj_ensayo_value = models.TextField(blank=True, null=True)
    field_tipo_obj_value = models.TextField(blank=True, null=True)
    field_otro_tipo_obj_value = models.TextField(blank=True, null=True)
    field_hipotesis_value = models.TextField(blank=True, null=True)
    field_variable_prim_value = models.TextField(blank=True, null=True)
    field_variable_secund_value = models.TextField(blank=True, null=True)
    field_genero_value = models.TextField(blank=True, null=True)
    field_edad_min_value = models.TextField(blank=True, null=True)
    field_edad_max_value = models.TextField(blank=True, null=True)
    field_criterio_inclus_value = models.TextField(blank=True, null=True)
    field_criterio_exclus_value = models.TextField(blank=True, null=True)
    field_tipo_poblacion_value = models.TextField(blank=True, null=True)
    field_tipo_participacion_value = models.TextField(blank=True, null=True)
    field_tipo_estudio_value = models.TextField(blank=True, null=True)
    field_aleatorizacion_value = models.TextField(blank=True, null=True)
    field_enmascarameinto_value = models.TextField(blank=True, null=True)
    field_grupo_control_value = models.TextField(blank=True, null=True)
    field_diseno_value = models.TextField(blank=True, null=True)
    field_otro_diseno_value = models.TextField(blank=True, null=True)
    field_otro_det_diseno_value = models.TextField(blank=True, null=True)
    field_prop_primario_value = models.TextField(blank=True, null=True)
    field_otro_proposito_value = models.TextField(blank=True, null=True)
    field_fase_value = models.TextField(blank=True, null=True)
    field_tamano_muestra_value = models.TextField(blank=True, null=True)
    field_1er_contacto_gener_value = models.TextField(blank=True, null=True)
    field_2do_contacto_gener_value = models.TextField(blank=True, null=True)
    field_apell_contacto_gener_value = models.TextField(blank=True, null=True)
    field_esp_contacto_gener_value = models.TextField(blank=True, null=True)
    field_trab_contacto_gener_value = models.TextField(blank=True, null=True)
    field_dir_contacto_gener_value = models.TextField(blank=True, null=True)
    field_prov_contacto_value = models.TextField(blank=True, null=True)
    field_pais_contacto_gener_value = models.TextField(blank=True, null=True)
    field_cod_contacto_gener_value = models.TextField(blank=True, null=True)
    field_tel_contacto_gen_value = models.TextField(blank=True, null=True)
    field_1er_contacto_cient_value = models.TextField(blank=True, null=True)
    field_2do_contacto_cient_value = models.TextField(blank=True, null=True)
    field_apell_contacto_cient_value = models.TextField(blank=True, null=True)
    field_esp_contacto_cient_value = models.TextField(blank=True, null=True)
    field_trab_contacto_cient_value = models.TextField(blank=True, null=True)
    field_dir_contacto_cient_value = models.TextField(blank=True, null=True)
    field_prov_contacto_cient_value = models.TextField(blank=True, null=True)
    field_pais_contacto_cient_value = models.TextField(blank=True, null=True)
    field_cod_contacto_cient_value = models.TextField(blank=True, null=True)
    field_tel_contacto_cient_value = models.TextField(blank=True, null=True)
    field_referencia_value = models.TextField(blank=True, null=True)
    field_resultado_value = models.TextField(blank=True, null=True)
    field_nomb_reg_publico_value = models.TextField(blank=True, null=True)
    field_cod_reg_pub_value = models.TextField(blank=True, null=True)
    field_fecha_reg_ens_value = models.TextField(blank=True, null=True)
    field_fecha_ult_act_value = models.TextField(blank=True, null=True)
    field_fecha_prox_act_value = models.TextField(blank=True, null=True)
    field_uri_value = models.TextField(blank=True, null=True)
    field_uri_format = models.PositiveIntegerField(blank=True, null=True)
    field_escrito_por_value = models.TextField(blank=True, null=True)
    field_add_diseno_value = models.TextField(blank=True, null=True)
    field_plan_int_datos_value = models.TextField(blank=True, null=True)
    field_des_datos_value = models.TextField(blank=True, null=True)
    field_informacion_compartir_value = models.TextField(blank=True, null=True)
    field_url_inf_adicional_value = models.TextField(blank=True, null=True)
    field_term_estudio_value = models.CharField(max_length=20, blank=True, null=True)
    field_disp_resultados_value = models.CharField(max_length=20, blank=True, null=True)
    field_primera_pub_value = models.CharField(max_length=20, blank=True, null=True)
    field_flujo_participantes_value = models.TextField(blank=True, null=True)
    field_datos_basales_value = models.TextField(blank=True, null=True)
    field_res_prim_sec_value = models.TextField(blank=True, null=True)
    field_eventos_adversos_value = models.TextField(blank=True, null=True)
    field_resumen_value = models.TextField(blank=True, null=True)
    field_subir_resultado_fid = models.IntegerField(blank=True, null=True)
    field_subir_resultado_list = models.IntegerField(blank=True, null=True)
    field_subir_resultado_data = models.TextField(blank=True, null=True)
    field_subir_comite_fid = models.IntegerField(blank=True, null=True)
    field_subir_comite_list = models.IntegerField(blank=True, null=True)
    field_subir_comite_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_type_ensayos_clinicos'


class ContentFieldInstProducto(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_inst_producto_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_inst_producto'
        unique_together = (('vid', 'delta'),)


class ContentFieldNumeroReg(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_numero_reg_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_numero_reg'
        unique_together = (('vid', 'delta'),)


class ContentFieldFechaRegistro(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_fecha_registro_value = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_fecha_registro'
        unique_together = (('vid', 'delta'),)


class ContentFieldTelefInvestigador(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_telef_investigador_number = models.CharField(max_length=15, blank=True, null=True)
    field_telef_investigador_country_codes = models.CharField(max_length=2, blank=True, null=True)
    field_telef_investigador_extension = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_telef_investigador'
        unique_together = (('vid', 'delta'),)


class ContentFieldCorreoInvestigador(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_correo_investigador_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_correo_investigador'
        unique_together = (('vid', 'delta'),)


class ContentFieldCodigoCm(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_codigo_cm_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_codigo_cm'
        unique_together = (('vid', 'delta'),)


class ContentFieldCodigoIntervencion(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_codigo_intervencion_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_codigo_intervencion'
        unique_together = (('vid', 'delta'),)


class ContentFieldCorreoContactoGener(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_correo_contacto_gener_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_correo_contacto_gener'
        unique_together = (('vid', 'delta'),)


class ContentFieldCorreoContactoCient(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_correo_contacto_cient_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_correo_contacto_cient'
        unique_together = (('vid', 'delta'),)
