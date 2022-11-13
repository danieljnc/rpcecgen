# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Access(models.Model):
    aid = models.AutoField(primary_key=True)
    mask = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'access'


class Actions(models.Model):
    aid = models.CharField(primary_key=True, max_length=255)
    type = models.CharField(max_length=32)
    callback = models.CharField(max_length=255)
    parameters = models.TextField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'actions'


class ActionsAid(models.Model):
    aid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'actions_aid'


class AdvancedHelpIndex(models.Model):
    sid = models.AutoField(primary_key=True)
    module = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    language = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'advanced_help_index'


class Authmap(models.Model):
    aid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    authname = models.CharField(unique=True, max_length=128)
    module = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'authmap'


class BackupMigrateDestinations(models.Model):
    destination_id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=32)
    location = models.TextField()
    settings = models.TextField()

    class Meta:
        managed = False
        db_table = 'backup_migrate_destinations'


class BackupMigrateProfiles(models.Model):
    profile_id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    filename = models.CharField(max_length=50)
    append_timestamp = models.PositiveIntegerField()
    timestamp_format = models.CharField(max_length=14)
    filters = models.TextField()

    class Meta:
        managed = False
        db_table = 'backup_migrate_profiles'


class BackupMigrateSchedules(models.Model):
    schedule_id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    source_id = models.CharField(max_length=32)
    destination_id = models.CharField(max_length=32)
    profile_id = models.CharField(max_length=32)
    keep = models.IntegerField()
    period = models.IntegerField()
    last_run = models.IntegerField()
    enabled = models.PositiveIntegerField()
    cron = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'backup_migrate_schedules'


class Batch(models.Model):
    bid = models.AutoField(primary_key=True)
    token = models.CharField(max_length=64)
    timestamp = models.IntegerField()
    batch = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batch'


class Blocks(models.Model):
    bid = models.AutoField(primary_key=True)
    module = models.CharField(max_length=64)
    delta = models.CharField(max_length=32)
    theme = models.CharField(max_length=64)
    status = models.IntegerField()
    weight = models.IntegerField()
    region = models.CharField(max_length=64)
    custom = models.IntegerField()
    throttle = models.IntegerField()
    visibility = models.IntegerField()
    pages = models.TextField()
    title = models.CharField(max_length=64)
    cache = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blocks'
        unique_together = (('theme', 'module', 'delta'),)


class BlocksRoles(models.Model):
    module = models.CharField(primary_key=True, max_length=64)
    delta = models.CharField(max_length=32)
    rid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'blocks_roles'
        unique_together = (('module', 'delta', 'rid'),)


class Boxes(models.Model):
    bid = models.AutoField(primary_key=True)
    body = models.TextField(blank=True, null=True)
    info = models.CharField(unique=True, max_length=128)
    format = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'boxes'


class Cache(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache'


class CacheAdminMenu(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_admin_menu'


class CacheBlock(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_block'


class CacheContent(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_content'


class CacheFilter(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_filter'


class CacheForm(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_form'


class CacheL10NUpdate(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_l10n_update'


class CacheMenu(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_menu'


class CachePage(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_page'


class CacheRules(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_rules'


class CacheUpdate(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_update'


class CacheViews(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_views'


class CacheViewsData(models.Model):
    cid = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)
    expire = models.IntegerField()
    created = models.IntegerField()
    headers = models.TextField(blank=True, null=True)
    serialized = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cache_views_data'


class CaptchaPoints(models.Model):
    form_id = models.CharField(primary_key=True, max_length=128)
    module = models.CharField(max_length=64, blank=True, null=True)
    captcha_type = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'captcha_points'


class CaptchaSessions(models.Model):
    csid = models.AutoField(primary_key=True)
    token = models.CharField(max_length=64, blank=True, null=True)
    uid = models.IntegerField()
    sid = models.CharField(max_length=64)
    ip_address = models.CharField(max_length=128, blank=True, null=True)
    timestamp = models.IntegerField()
    form_id = models.CharField(max_length=128)
    solution = models.CharField(max_length=128)
    status = models.IntegerField()
    attempts = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'captcha_sessions'


class Comments(models.Model):
    cid = models.AutoField(primary_key=True)
    pid = models.IntegerField()
    nid = models.IntegerField()
    uid = models.IntegerField()
    subject = models.CharField(max_length=64)
    comment = models.TextField()
    hostname = models.CharField(max_length=128)
    timestamp = models.IntegerField()
    status = models.PositiveIntegerField()
    format = models.SmallIntegerField()
    thread = models.CharField(max_length=255)
    name = models.CharField(max_length=60, blank=True, null=True)
    mail = models.CharField(max_length=64, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class ConditionalFields(models.Model):
    control_field_name = models.CharField(primary_key=True, max_length=32)
    field_name = models.CharField(max_length=32)
    type = models.CharField(max_length=127)
    trigger_values = models.TextField()

    class Meta:
        managed = False
        db_table = 'conditional_fields'
        unique_together = (('control_field_name', 'field_name', 'type'),)


class Contact(models.Model):
    cid = models.AutoField(primary_key=True)
    category = models.CharField(unique=True, max_length=255)
    recipients = models.TextField()
    reply = models.TextField()
    weight = models.IntegerField()
    selected = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'contact'


class Contemplate(models.Model):
    type = models.CharField(max_length=32)
    teaser = models.TextField()
    body = models.TextField()
    rss = models.TextField()
    enclosure = models.CharField(max_length=128)
    flags = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'contemplate'


class ContemplateFiles(models.Model):
    site = models.CharField(unique=True, max_length=255)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'contemplate_files'


class ContentFieldAprobaciones(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_aprobaciones_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_aprobaciones'
        unique_together = (('vid', 'delta'),)


class ContentFieldAsignoCodigo(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_asigno_codigo_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_asigno_codigo'
        unique_together = (('vid', 'delta'),)


class ContentFieldAuthorityIdentifying(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_authority_identifying_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_authority_identifying'
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


class ContentFieldComiteEtica(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_comite_etica_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_comite_etica'
        unique_together = (('vid', 'delta'),)


class ContentFieldCommmitteFhone(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_commmitte_fhone_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_commmitte_fhone'
        unique_together = (('vid', 'delta'),)


class ContentFieldCommmitteMail(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_commmitte_mail_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_commmitte_mail'
        unique_together = (('vid', 'delta'),)


class ContentFieldCorreoComEtica(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_correo_com_etica_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_correo_com_etica'
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


class ContentFieldCorreoContactoGener(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_correo_contacto_gener_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_correo_contacto_gener'
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


class ContentFieldCountries(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_countries_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_countries'
        unique_together = (('vid', 'delta'),)


class ContentFieldDateCommittee(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_date_committee_value = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_date_committee'
        unique_together = (('vid', 'delta'),)


class ContentFieldDocument(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_document_fid = models.IntegerField(blank=True, null=True)
    field_document_list = models.IntegerField(blank=True, null=True)
    field_document_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_document'
        unique_together = (('vid', 'delta'),)


class ContentFieldEmailInvestigator(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_email_investigator_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_email_investigator'
        unique_together = (('vid', 'delta'),)


class ContentFieldEmailPublic(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_email_public_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_email_public'
        unique_together = (('vid', 'delta'),)


class ContentFieldEmailScientific(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_email_scientific_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_email_scientific'
        unique_together = (('vid', 'delta'),)


class ContentFieldEstadoEval(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_estado_eval_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_estado_eval'
        unique_together = (('vid', 'delta'),)


class ContentFieldEthicsCommittes(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_ethics_committes_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_ethics_committes'
        unique_together = (('vid', 'delta'),)


class ContentFieldEvaluationStatus(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_evaluation_status_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_evaluation_status'
        unique_together = (('vid', 'delta'),)


class ContentFieldFechaEtica(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_fecha_etica_value = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_fecha_etica'
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


class ContentFieldHcCode(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_hc_code_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_hc_code'
        unique_together = (('vid', 'delta'),)


class ContentFieldHcKeyword(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_hc_keyword_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_hc_keyword'
        unique_together = (('vid', 'delta'),)


class ContentFieldIdentificador(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_identificador_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_identificador'
        unique_together = (('vid', 'delta'),)


class ContentFieldIdentifying(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_identifying_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_identifying'
        unique_together = (('vid', 'delta'),)


class ContentFieldInstProducto(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_inst_producto_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_inst_producto'
        unique_together = (('vid', 'delta'),)


class ContentFieldInterCode(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_inter_code_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_inter_code'
        unique_together = (('vid', 'delta'),)


class ContentFieldInvestigatorPhone(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_investigator_phone_number = models.CharField(max_length=15, blank=True, null=True)
    field_investigator_phone_country_codes = models.CharField(max_length=2, blank=True, null=True)
    field_investigator_phone_extension = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_investigator_phone'
        unique_together = (('vid', 'delta'),)


class ContentFieldModificaciones(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_modificaciones_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_modificaciones'
        unique_together = (('vid', 'delta'),)


class ContentFieldNombreEtica(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_nombre_etica_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_nombre_etica'
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


class ContentFieldOtroPromotor(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_otro_promotor_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_otro_promotor'
        unique_together = (('vid', 'delta'),)


class ContentFieldPaise(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_paise_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_paise'
        unique_together = (('vid', 'delta'),)


class ContentFieldParticipatingSc(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_participating_sc_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_participating_sc'
        unique_together = (('vid', 'delta'),)


class ContentFieldPublicPhone(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_public_phone_number = models.CharField(max_length=15, blank=True, null=True)
    field_public_phone_country_codes = models.CharField(max_length=2, blank=True, null=True)
    field_public_phone_extension = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_public_phone'
        unique_together = (('vid', 'delta'),)


class ContentFieldResearchCommittee(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_research_committee_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_research_committee'
        unique_together = (('vid', 'delta'),)


class ContentFieldScParticipantes(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_sc_participantes_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_sc_participantes'
        unique_together = (('vid', 'delta'),)


class ContentFieldScientificPhone(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_scientific_phone_number = models.CharField(max_length=15, blank=True, null=True)
    field_scientific_phone_country_codes = models.CharField(max_length=2, blank=True, null=True)
    field_scientific_phone_extension = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_scientific_phone'
        unique_together = (('vid', 'delta'),)


class ContentFieldSecSponsor(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_sec_sponsor_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_sec_sponsor'
        unique_together = (('vid', 'delta'),)


class ContentFieldSubir(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_subir_fid = models.IntegerField(blank=True, null=True)
    field_subir_list = models.IntegerField(blank=True, null=True)
    field_subir_data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_subir'
        unique_together = (('vid', 'delta'),)


class ContentFieldTeleOrg(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_tele_org_number = models.CharField(max_length=15, blank=True, null=True)
    field_tele_org_country_codes = models.CharField(max_length=2, blank=True, null=True)
    field_tele_org_extension = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_tele_org'
        unique_together = (('vid', 'delta'),)


class ContentFieldTeleRepresentante(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_tele_representante_number = models.CharField(max_length=15, blank=True, null=True)
    field_tele_representante_country_codes = models.CharField(max_length=2, blank=True, null=True)
    field_tele_representante_extension = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_tele_representante'
        unique_together = (('vid', 'delta'),)


class ContentFieldTelefComEtica(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_telef_com_etica_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_telef_com_etica'
        unique_together = (('vid', 'delta'),)


class ContentFieldTelefContactoCient(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_telef_contacto_cient_number = models.CharField(max_length=15, blank=True, null=True)
    field_telef_contacto_cient_country_codes = models.CharField(max_length=2, blank=True, null=True)
    field_telef_contacto_cient_extension = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_telef_contacto_cient'
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


class ContentFieldUrlCommittees(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_url_committees_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_url_committees'
        unique_together = (('vid', 'delta'),)


class ContentFieldZipComEtica(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_zip_com_etica_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_zip_com_etica'
        unique_together = (('vid', 'delta'),)


class ContentFieldZipCommittee(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_zip_committee_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_zip_committee'
        unique_together = (('vid', 'delta'),)


class ContentGroup(models.Model):
    group_type = models.CharField(max_length=32)
    type_name = models.CharField(primary_key=True, max_length=32)
    group_name = models.CharField(max_length=32)
    label = models.CharField(max_length=255)
    settings = models.TextField()
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'content_group'
        unique_together = (('type_name', 'group_name'),)


class ContentGroupFields(models.Model):
    type_name = models.CharField(primary_key=True, max_length=32)
    group_name = models.CharField(max_length=32)
    field_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'content_group_fields'
        unique_together = (('type_name', 'group_name', 'field_name'),)


class ContentNodeField(models.Model):
    field_name = models.CharField(primary_key=True, max_length=32)
    type = models.CharField(max_length=127)
    global_settings = models.TextField()
    required = models.IntegerField()
    multiple = models.IntegerField()
    db_storage = models.IntegerField()
    module = models.CharField(max_length=127)
    db_columns = models.TextField()
    active = models.IntegerField()
    locked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'content_node_field'


class ContentNodeFieldInstance(models.Model):
    field_name = models.CharField(primary_key=True, max_length=32)
    type_name = models.CharField(max_length=32)
    weight = models.IntegerField()
    label = models.CharField(max_length=255)
    widget_type = models.CharField(max_length=32)
    widget_settings = models.TextField()
    display_settings = models.TextField()
    description = models.TextField()
    widget_module = models.CharField(max_length=127)
    widget_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'content_node_field_instance'
        unique_together = (('field_name', 'type_name'),)


class ContentTypeArchivos(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    field_criterios_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_type_archivos'


class ContentTypeClinicalTrials(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    field_scientific_title_value = models.TextField(blank=True, null=True)
    field_scientific_acronym_value = models.TextField(blank=True, null=True)
    field_sponsor_value = models.TextField(blank=True, null=True)
    field_reg_instance_value = models.TextField(blank=True, null=True)
    field_regulatiry_inst_value = models.TextField(blank=True, null=True)
    field_other_instances_value = models.TextField(blank=True, null=True)
    field_date_notification_value = models.DateTimeField(blank=True, null=True)
    field_authorization_date_value = models.DateTimeField(blank=True, null=True)
    field_ref_number_value = models.TextField(blank=True, null=True)
    field_first_investigator_value = models.TextField(blank=True, null=True)
    field_midle_investigator_value = models.TextField(blank=True, null=True)
    field_last_investigator_value = models.TextField(blank=True, null=True)
    field_affiliation_value = models.TextField(blank=True, null=True)
    field_code_investigator_value = models.TextField(blank=True, null=True)
    field_address_investigator_value = models.TextField(blank=True, null=True)
    field_city_investigator_value = models.TextField(blank=True, null=True)
    field_country_investigator_value = models.TextField(blank=True, null=True)
    field_recruitment_status_value = models.TextField(blank=True, null=True)
    field_date_first_enrollment_value = models.DateTimeField(blank=True, null=True)
    field_health_condition_value = models.TextField(blank=True, null=True)
    field_intervention_value = models.TextField(blank=True, null=True)
    field_primary_outcomes_value = models.TextField(blank=True, null=True)
    field_secondary_outcomes_value = models.TextField(blank=True, null=True)
    field_gender_value = models.TextField(blank=True, null=True)
    field_minimum_age_value = models.TextField(blank=True, null=True)
    field_maximum_age_value = models.TextField(blank=True, null=True)
    field_inclusion_criteria_value = models.TextField(blank=True, null=True)
    field_exclusion_criteria_value = models.TextField(blank=True, null=True)
    field_type_participant_value = models.TextField(blank=True, null=True)
    field_type_study_value = models.TextField(blank=True, null=True)
    field_allocation_value = models.TextField(blank=True, null=True)
    field_masking_value = models.TextField(blank=True, null=True)
    field_control_group_value = models.TextField(blank=True, null=True)
    field_study_design_value = models.TextField(blank=True, null=True)
    field_other_design_value = models.TextField(blank=True, null=True)
    field_purpose_value = models.TextField(blank=True, null=True)
    field_other_purpose_value = models.TextField(blank=True, null=True)
    field_phase_value = models.TextField(blank=True, null=True)
    field_target_sample_size_value = models.TextField(blank=True, null=True)
    field_firstname_public_value = models.TextField(blank=True, null=True)
    field_midlename_public_value = models.TextField(blank=True, null=True)
    field_lastname_public_value = models.TextField(blank=True, null=True)
    field_affiliation_public_value = models.TextField(blank=True, null=True)
    field_address_public_value = models.TextField(blank=True, null=True)
    field_city_public_value = models.TextField(blank=True, null=True)
    field_country_public_value = models.TextField(blank=True, null=True)
    field_zipcode_public_value = models.TextField(blank=True, null=True)
    field_firstname_scientific_value = models.TextField(blank=True, null=True)
    field_midlename_scientfic_value = models.TextField(blank=True, null=True)
    field_lastname_scientific_value = models.TextField(blank=True, null=True)
    field_affiliation_scientific_value = models.TextField(blank=True, null=True)
    field_address_scientific_value = models.TextField(blank=True, null=True)
    field_city_scientific_value = models.TextField(blank=True, null=True)
    field_country_scientific_value = models.TextField(blank=True, null=True)
    field_zipcode_scientific_value = models.TextField(blank=True, null=True)
    field_primary_registry_value = models.TextField(blank=True, null=True)
    field_id_number_value = models.TextField(blank=True, null=True)
    field_public_acronym_value = models.TextField(blank=True, null=True)
    field_spec_investigator_value = models.TextField(blank=True, null=True)
    field_type_population_value = models.TextField(blank=True, null=True)
    field_specialty_public_value = models.TextField(blank=True, null=True)
    field_specialty_scientific_value = models.TextField(blank=True, null=True)
    field_date_register_value = models.TextField(blank=True, null=True)
    field_record_verification_value = models.TextField(blank=True, null=True)
    field_update_date_value = models.TextField(blank=True, null=True)
    field_i_keyword_value = models.TextField(blank=True, null=True)
    field_source_monetary_value = models.TextField(blank=True, null=True)
    field_tel_contact_gen_value = models.TextField(blank=True, null=True)
    field_tel_contact_cient_value = models.TextField(blank=True, null=True)
    field_uri_ct_value = models.TextField(blank=True, null=True)
    field_uri_ct_format = models.PositiveIntegerField(blank=True, null=True)
    field_actual_enroment_value = models.TextField(blank=True, null=True)
    field_data_plan_value = models.TextField(blank=True, null=True)
    field_des_plan_value = models.TextField(blank=True, null=True)
    field_aditional_documents_value = models.TextField(blank=True, null=True)
    field_url_documents_value = models.TextField(blank=True, null=True)
    field_study_date_value = models.CharField(max_length=20, blank=True, null=True)
    field_results_date_value = models.CharField(max_length=20, blank=True, null=True)
    field_first_publication_value = models.CharField(max_length=20, blank=True, null=True)
    field_par_flow_value = models.TextField(blank=True, null=True)
    field_base_charat_value = models.TextField(blank=True, null=True)
    field_out_measures_value = models.TextField(blank=True, null=True)
    field_adv_events_value = models.TextField(blank=True, null=True)
    field_summary_value = models.TextField(blank=True, null=True)
    field_upload_results_fid = models.IntegerField(blank=True, null=True)
    field_upload_results_list = models.IntegerField(blank=True, null=True)
    field_upload_results_data = models.TextField(blank=True, null=True)
    field_change_value = models.TextField(blank=True, null=True)
    field_results_url_link_value = models.TextField(blank=True, null=True)
    field_results2_url_link_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_type_clinical_trials'


class ContentTypeDate(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    field_date_value = models.DateTimeField(blank=True, null=True)
    field_date_value2 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_type_date'


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


class ContentTypeProfile(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    field_pais_org_value = models.CharField(max_length=2, blank=True, null=True)
    field_tipo_org_value = models.TextField(blank=True, null=True)
    field_nombre_org_value = models.TextField(blank=True, null=True)
    field_sigla_org_value = models.TextField(blank=True, null=True)
    field_direccion_org_value = models.TextField(blank=True, null=True)
    field_correo_org_email = models.CharField(max_length=255, blank=True, null=True)
    field_sitioweb_org_url = models.CharField(max_length=2048, blank=True, null=True)
    field_sitioweb_org_title = models.CharField(max_length=255, blank=True, null=True)
    field_sitioweb_org_attributes = models.TextField(blank=True, null=True)
    field_representante_oficial_value = models.TextField(blank=True, null=True)
    field_nombre_en_org_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_type_profile'


class ContinentsApiContinents(models.Model):
    continent = models.CharField(primary_key=True, max_length=2)
    country = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'continents_api_continents'
        unique_together = (('continent', 'country'),)


class CountriesApiCountries(models.Model):
    iso2 = models.CharField(primary_key=True, max_length=2)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    name = models.CharField(max_length=80)
    printable_name = models.CharField(max_length=80)
    numcode = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries_api_countries'


class CtoolsAccessRuleset(models.Model):
    rsid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    admin_title = models.CharField(max_length=255, blank=True, null=True)
    admin_description = models.TextField(blank=True, null=True)
    requiredcontexts = models.TextField(blank=True, null=True)
    contexts = models.TextField(blank=True, null=True)
    relationships = models.TextField(blank=True, null=True)
    access = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctools_access_ruleset'


class CtoolsCssCache(models.Model):
    cid = models.CharField(primary_key=True, max_length=128)
    filename = models.CharField(max_length=255, blank=True, null=True)
    css = models.TextField(blank=True, null=True)
    filter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctools_css_cache'


class CtoolsCustomContent(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    admin_title = models.CharField(max_length=255, blank=True, null=True)
    admin_description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctools_custom_content'


class CtoolsObjectCache(models.Model):
    sid = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=128)
    obj = models.CharField(max_length=32)
    updated = models.PositiveIntegerField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctools_object_cache'
        unique_together = (('sid', 'obj', 'name'),)


class DateFormatLocale(models.Model):
    format = models.CharField(max_length=100)
    type = models.CharField(primary_key=True, max_length=200)
    language = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'date_format_locale'
        unique_together = (('type', 'language'),)


class DateFormatTypes(models.Model):
    type = models.CharField(primary_key=True, max_length=200)
    title = models.CharField(max_length=255)
    locked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'date_format_types'


class DateFormats(models.Model):
    dfid = models.AutoField(primary_key=True)
    format = models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    locked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'date_formats'
        unique_together = (('format', 'type'),)


class DatosInternosRpcec(models.Model):
    cod_rpcec = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_internos_rpcec'


class DevelQueries(models.Model):
    qid = models.AutoField()
    function = models.CharField(max_length=255)
    query = models.TextField()
    hash = models.CharField(primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'devel_queries'


class DevelTimes(models.Model):
    tid = models.AutoField(primary_key=True)
    qid = models.IntegerField()
    time = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devel_times'


class FaqQuestions(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    vid = models.PositiveIntegerField()
    question = models.TextField()
    detailed_question = models.TextField()

    class Meta:
        managed = False
        db_table = 'faq_questions'
        unique_together = (('nid', 'vid'),)


class FaqWeights(models.Model):
    tid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField(primary_key=True)
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'faq_weights'
        unique_together = (('nid', 'tid'),)


class Files(models.Model):
    fid = models.AutoField(primary_key=True)
    uid = models.PositiveIntegerField()
    filename = models.CharField(max_length=255)
    filepath = models.CharField(max_length=255)
    filemime = models.CharField(max_length=255)
    filesize = models.PositiveIntegerField()
    status = models.IntegerField()
    timestamp = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'files'


class FilterFormats(models.Model):
    format = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    roles = models.CharField(max_length=255)
    cache = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filter_formats'


class Filters(models.Model):
    fid = models.AutoField(primary_key=True)
    format = models.IntegerField()
    module = models.CharField(max_length=64)
    delta = models.IntegerField()
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'filters'
        unique_together = (('format', 'module', 'delta'),)


class Flood(models.Model):
    fid = models.AutoField(primary_key=True)
    event = models.CharField(max_length=64)
    hostname = models.CharField(max_length=128)
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'flood'


class History(models.Model):
    uid = models.IntegerField(primary_key=True)
    nid = models.IntegerField()
    timestamp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history'
        unique_together = (('uid', 'nid'),)


class I18NBlocks(models.Model):
    ibid = models.AutoField(primary_key=True)
    module = models.CharField(max_length=64)
    delta = models.CharField(max_length=32)
    type = models.IntegerField()
    language = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'i18n_blocks'


class I18NStrings(models.Model):
    lid = models.IntegerField(primary_key=True)
    objectid = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    property = models.CharField(max_length=255)
    objectindex = models.IntegerField()
    format = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'i18n_strings'


class I18NVariable(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    language = models.CharField(max_length=12)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'i18n_variable'
        unique_together = (('name', 'language'),)


class L10NUpdateFile(models.Model):
    project = models.CharField(primary_key=True, max_length=50)
    language = models.CharField(max_length=12)
    type = models.CharField(max_length=50)
    filename = models.CharField(max_length=255)
    fileurl = models.CharField(max_length=255)
    filepath = models.CharField(max_length=255)
    timestamp = models.IntegerField(blank=True, null=True)
    version = models.CharField(max_length=128)
    status = models.IntegerField()
    last_checked = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l10n_update_file'
        unique_together = (('project', 'language'),)


class L10NUpdateProject(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    project_type = models.CharField(max_length=50)
    core = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    l10n_server = models.CharField(max_length=255)
    l10n_path = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'l10n_update_project'


class Languages(models.Model):
    language = models.CharField(primary_key=True, max_length=12)
    name = models.CharField(max_length=64)
    native = models.CharField(max_length=64)
    direction = models.IntegerField()
    enabled = models.IntegerField()
    plurals = models.IntegerField()
    formula = models.CharField(max_length=128)
    domain = models.CharField(max_length=128)
    prefix = models.CharField(max_length=128)
    weight = models.IntegerField()
    javascript = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'languages'


class LocalesSource(models.Model):
    lid = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    textgroup = models.CharField(max_length=255)
    source = models.TextField()
    version = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'locales_source'


class LocalesTarget(models.Model):
    lid = models.IntegerField()
    translation = models.TextField()
    language = models.CharField(primary_key=True, max_length=12)
    plid = models.IntegerField()
    plural = models.IntegerField()
    i18n_status = models.IntegerField()
    l10n_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'locales_target'
        unique_together = (('language', 'lid', 'plural'),)


class MenuCustom(models.Model):
    menu_name = models.CharField(primary_key=True, max_length=32)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_custom'


class MenuLinks(models.Model):
    menu_name = models.CharField(max_length=32)
    mlid = models.AutoField(primary_key=True)
    plid = models.PositiveIntegerField()
    link_path = models.CharField(max_length=255)
    router_path = models.CharField(max_length=255)
    link_title = models.CharField(max_length=255)
    options = models.TextField(blank=True, null=True)
    module = models.CharField(max_length=255)
    hidden = models.SmallIntegerField()
    external = models.SmallIntegerField()
    has_children = models.SmallIntegerField()
    expanded = models.SmallIntegerField()
    weight = models.IntegerField()
    depth = models.SmallIntegerField()
    customized = models.SmallIntegerField()
    p1 = models.PositiveIntegerField()
    p2 = models.PositiveIntegerField()
    p3 = models.PositiveIntegerField()
    p4 = models.PositiveIntegerField()
    p5 = models.PositiveIntegerField()
    p6 = models.PositiveIntegerField()
    p7 = models.PositiveIntegerField()
    p8 = models.PositiveIntegerField()
    p9 = models.PositiveIntegerField()
    updated = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'menu_links'


class MenuRouter(models.Model):
    path = models.CharField(primary_key=True, max_length=255)
    load_functions = models.TextField()
    to_arg_functions = models.TextField()
    access_callback = models.CharField(max_length=255)
    access_arguments = models.TextField(blank=True, null=True)
    page_callback = models.CharField(max_length=255)
    page_arguments = models.TextField(blank=True, null=True)
    fit = models.IntegerField()
    number_parts = models.SmallIntegerField()
    tab_parent = models.CharField(max_length=255)
    tab_root = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    title_callback = models.CharField(max_length=255)
    title_arguments = models.CharField(max_length=255)
    type = models.IntegerField()
    block_callback = models.CharField(max_length=255)
    description = models.TextField()
    position = models.CharField(max_length=255)
    weight = models.IntegerField()
    file = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu_router'


class Multistep(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    step = models.PositiveIntegerField()
    status = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'multistep'
        unique_together = (('nid', 'step'),)


class Node(models.Model):
    nid = models.AutoField(primary_key=True)
    vid = models.PositiveIntegerField(unique=True)
    type = models.CharField(max_length=32)
    language = models.CharField(max_length=12)
    title = models.CharField(max_length=255)
    uid = models.IntegerField()
    status = models.IntegerField()
    created = models.IntegerField()
    changed = models.IntegerField()
    comment = models.IntegerField()
    promote = models.IntegerField()
    moderate = models.IntegerField()
    sticky = models.IntegerField()
    tnid = models.PositiveIntegerField()
    translate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node'


class NodeAccess(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    gid = models.PositiveIntegerField()
    realm = models.CharField(max_length=255)
    grant_view = models.PositiveIntegerField()
    grant_update = models.PositiveIntegerField()
    grant_delete = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'node_access'
        unique_together = (('nid', 'gid', 'realm'),)


class NodeCommentStatistics(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    last_comment_timestamp = models.IntegerField()
    last_comment_name = models.CharField(max_length=60, blank=True, null=True)
    last_comment_uid = models.IntegerField()
    comment_count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'node_comment_statistics'


class NodeCounter(models.Model):
    nid = models.IntegerField(primary_key=True)
    totalcount = models.BigIntegerField()
    daycount = models.PositiveIntegerField()
    timestamp = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'node_counter'


class NodeImportStatus(models.Model):
    taskid = models.PositiveIntegerField(primary_key=True)
    file_offset = models.PositiveIntegerField()
    errors = models.TextField()
    objid = models.PositiveIntegerField()
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'node_import_status'
        unique_together = (('taskid', 'file_offset'),)


class NodeImportTasks(models.Model):
    taskid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    uid = models.PositiveIntegerField()
    created = models.PositiveIntegerField()
    changed = models.PositiveIntegerField()
    fid = models.PositiveIntegerField()
    has_headers = models.PositiveIntegerField()
    file_options = models.TextField()
    headers = models.TextField()
    type = models.CharField(max_length=64)
    map = models.TextField()
    defaults = models.TextField()
    options = models.TextField()
    file_offset = models.PositiveIntegerField()
    row_done = models.PositiveIntegerField()
    row_error = models.PositiveIntegerField()
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'node_import_tasks'


class NodeRevisions(models.Model):
    nid = models.PositiveIntegerField()
    vid = models.AutoField(primary_key=True)
    uid = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField()
    teaser = models.TextField()
    log = models.TextField()
    timestamp = models.IntegerField()
    format = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'node_revisions'


class NodeType(models.Model):
    type = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    description = models.TextField()
    help = models.TextField()
    has_title = models.PositiveIntegerField()
    title_label = models.CharField(max_length=255)
    has_body = models.PositiveIntegerField()
    body_label = models.CharField(max_length=255)
    min_word_count = models.PositiveSmallIntegerField()
    custom = models.IntegerField()
    modified = models.IntegerField()
    locked = models.IntegerField()
    orig_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'node_type'


class PageManagerHandlers(models.Model):
    did = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    task = models.CharField(max_length=64, blank=True, null=True)
    subtask = models.CharField(max_length=64)
    handler = models.CharField(max_length=64, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    conf = models.TextField()

    class Meta:
        managed = False
        db_table = 'page_manager_handlers'


class PageManagerPages(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    task = models.CharField(max_length=64, blank=True, null=True)
    admin_title = models.CharField(max_length=255, blank=True, null=True)
    admin_description = models.TextField(blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    access = models.TextField()
    menu = models.TextField()
    arguments = models.TextField()
    conf = models.TextField()

    class Meta:
        managed = False
        db_table = 'page_manager_pages'


class PageManagerWeights(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'page_manager_weights'


class PanelsDisplay(models.Model):
    did = models.AutoField(primary_key=True)
    layout = models.CharField(max_length=255, blank=True, null=True)
    layout_settings = models.TextField(blank=True, null=True)
    panel_settings = models.TextField(blank=True, null=True)
    cache = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    hide_title = models.IntegerField(blank=True, null=True)
    title_pane = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panels_display'


class PanelsLayout(models.Model):
    lid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    admin_title = models.CharField(max_length=255, blank=True, null=True)
    admin_description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    plugin = models.CharField(max_length=255, blank=True, null=True)
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panels_layout'


class PanelsMini(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    category = models.CharField(max_length=64, blank=True, null=True)
    did = models.IntegerField(blank=True, null=True)
    admin_title = models.CharField(max_length=128, blank=True, null=True)
    admin_description = models.TextField(blank=True, null=True)
    requiredcontexts = models.TextField(blank=True, null=True)
    contexts = models.TextField(blank=True, null=True)
    relationships = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panels_mini'


class PanelsNode(models.Model):
    nid = models.IntegerField()
    css_id = models.CharField(max_length=255, blank=True, null=True)
    did = models.IntegerField(primary_key=True)
    pipeline = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panels_node'


class PanelsPane(models.Model):
    pid = models.AutoField(primary_key=True)
    did = models.IntegerField()
    panel = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    subtype = models.CharField(max_length=64, blank=True, null=True)
    shown = models.IntegerField(blank=True, null=True)
    access = models.TextField(blank=True, null=True)
    configuration = models.TextField(blank=True, null=True)
    cache = models.TextField(blank=True, null=True)
    style = models.TextField(blank=True, null=True)
    css = models.TextField(blank=True, null=True)
    extras = models.TextField(blank=True, null=True)
    position = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panels_pane'


class PanelsRendererPipeline(models.Model):
    rpid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    admin_title = models.CharField(max_length=255, blank=True, null=True)
    admin_description = models.TextField(blank=True, null=True)
    weight = models.SmallIntegerField(blank=True, null=True)
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panels_renderer_pipeline'


class Permission(models.Model):
    pid = models.AutoField(primary_key=True)
    rid = models.PositiveIntegerField()
    perm = models.TextField(blank=True, null=True)
    tid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'permission'


class Poll(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    runtime = models.IntegerField()
    active = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'poll'


class PollChoices(models.Model):
    chid = models.AutoField(primary_key=True)
    nid = models.PositiveIntegerField()
    chtext = models.CharField(max_length=128)
    chvotes = models.IntegerField()
    chorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'poll_choices'


class PollVotes(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    uid = models.PositiveIntegerField()
    chorder = models.IntegerField()
    hostname = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'poll_votes'
        unique_together = (('nid', 'uid', 'hostname'),)


class PrintMailNodeConf(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    link = models.PositiveIntegerField()
    comments = models.PositiveIntegerField()
    url_list = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'print_mail_node_conf'


class PrintMailPageCounter(models.Model):
    path = models.CharField(primary_key=True, max_length=128)
    totalcount = models.BigIntegerField()
    timestamp = models.PositiveIntegerField()
    sentcount = models.BigIntegerField()
    sent_timestamp = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'print_mail_page_counter'


class PrintNodeConf(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    link = models.PositiveIntegerField()
    comments = models.PositiveIntegerField()
    url_list = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'print_node_conf'


class PrintPageCounter(models.Model):
    path = models.CharField(primary_key=True, max_length=128)
    totalcount = models.BigIntegerField()
    timestamp = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'print_page_counter'


class PrintPdfNodeConf(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    link = models.PositiveIntegerField()
    comments = models.PositiveIntegerField()
    url_list = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'print_pdf_node_conf'


class PrintPdfPageCounter(models.Model):
    path = models.CharField(primary_key=True, max_length=128)
    totalcount = models.BigIntegerField()
    timestamp = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'print_pdf_page_counter'


class ProfileFields(models.Model):
    fid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(unique=True, max_length=128)
    explanation = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    page = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=128, blank=True, null=True)
    weight = models.IntegerField()
    required = models.IntegerField()
    register = models.IntegerField()
    visibility = models.IntegerField()
    autocomplete = models.IntegerField()
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_fields'


class ProfileValues(models.Model):
    fid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField(primary_key=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_values'
        unique_together = (('uid', 'fid'),)


class RegionsApiRegions(models.Model):
    rid = models.AutoField(primary_key=True)
    iso2 = models.CharField(max_length=2)
    name = models.CharField(max_length=80)
    abbreviation = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions_api_regions'


class Role(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'role'


class RulesRules(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rules_rules'


class RulesScheduler(models.Model):
    tid = models.AutoField(primary_key=True)
    set_name = models.CharField(max_length=255)
    date = models.DateTimeField()
    arguments = models.TextField(blank=True, null=True)
    identifier = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rules_scheduler'


class RulesSets(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rules_sets'


class SearchDataset(models.Model):
    sid = models.PositiveIntegerField()
    type = models.CharField(max_length=16, blank=True, null=True)
    data = models.TextField()
    reindex = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'search_dataset'
        unique_together = (('sid', 'type'),)


class SearchIndex(models.Model):
    word = models.CharField(max_length=50)
    sid = models.PositiveIntegerField()
    type = models.CharField(max_length=16, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_index'
        unique_together = (('word', 'sid', 'type'),)


class SearchNodeLinks(models.Model):
    sid = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=16)
    nid = models.PositiveIntegerField()
    caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_node_links'
        unique_together = (('sid', 'type', 'nid'),)


class SearchTotal(models.Model):
    word = models.CharField(primary_key=True, max_length=50)
    count = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'search_total'


class Semaphore(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    value = models.CharField(max_length=255)
    expire = models.FloatField()

    class Meta:
        managed = False
        db_table = 'semaphore'


class ServicesEndpoint(models.Model):
    eid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    server = models.CharField(max_length=32)
    path = models.CharField(max_length=255)
    authentication = models.TextField()
    server_settings = models.TextField()
    resources = models.TextField()
    debug = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'services_endpoint'


class Sessions(models.Model):
    uid = models.PositiveIntegerField()
    sid = models.CharField(primary_key=True, max_length=64)
    hostname = models.CharField(max_length=128)
    timestamp = models.IntegerField()
    cache = models.IntegerField()
    session = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sessions'


class Stylizer(models.Model):
    sid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    admin_title = models.CharField(max_length=255, blank=True, null=True)
    admin_description = models.TextField(blank=True, null=True)
    settings = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stylizer'


class System(models.Model):
    filename = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    status = models.IntegerField()
    throttle = models.IntegerField()
    bootstrap = models.IntegerField()
    schema_version = models.SmallIntegerField()
    weight = models.IntegerField()
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system'


class TermData(models.Model):
    tid = models.AutoField(primary_key=True)
    vid = models.PositiveIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    weight = models.IntegerField()
    language = models.CharField(max_length=12)
    trid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'term_data'


class TermHierarchy(models.Model):
    tid = models.PositiveIntegerField(primary_key=True)
    parent = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'term_hierarchy'
        unique_together = (('tid', 'parent'),)


class TermNode(models.Model):
    nid = models.PositiveIntegerField()
    vid = models.PositiveIntegerField()
    tid = models.PositiveIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'term_node'
        unique_together = (('tid', 'vid'),)


class TermRelation(models.Model):
    trid = models.AutoField(primary_key=True)
    tid1 = models.PositiveIntegerField()
    tid2 = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'term_relation'
        unique_together = (('tid1', 'tid2'),)


class TermSynonym(models.Model):
    tsid = models.AutoField(primary_key=True)
    tid = models.PositiveIntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'term_synonym'


class TriggerAssignments(models.Model):
    hook = models.CharField(primary_key=True, max_length=32)
    op = models.CharField(max_length=32)
    aid = models.CharField(max_length=255)
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'trigger_assignments'
        unique_together = (('hook', 'op', 'aid'),)


class Upload(models.Model):
    fid = models.PositiveIntegerField()
    nid = models.PositiveIntegerField()
    vid = models.PositiveIntegerField(primary_key=True)
    description = models.CharField(max_length=255)
    list = models.PositiveIntegerField()
    weight = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'upload'
        unique_together = (('vid', 'fid'),)


class UrlAlias(models.Model):
    pid = models.AutoField(primary_key=True)
    src = models.CharField(max_length=128)
    dst = models.CharField(max_length=128)
    language = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'url_alias'
        unique_together = (('dst', 'language', 'pid'),)


class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=60)
    pass_field = models.CharField(db_column='pass', max_length=32)  # Field renamed because it was a Python reserved word.
    mail = models.CharField(max_length=64, blank=True, null=True)
    mode = models.IntegerField()
    sort = models.IntegerField(blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)
    theme = models.CharField(max_length=255)
    signature = models.CharField(max_length=255)
    signature_format = models.SmallIntegerField()
    created = models.IntegerField()
    access = models.IntegerField()
    login = models.IntegerField()
    status = models.IntegerField()
    timezone = models.CharField(max_length=8, blank=True, null=True)
    language = models.CharField(max_length=12)
    picture = models.CharField(max_length=255)
    init = models.CharField(max_length=64, blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    timezone_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users'


class UsersRoles(models.Model):
    uid = models.PositiveIntegerField(primary_key=True)
    rid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'users_roles'
        unique_together = (('uid', 'rid'),)


class Variable(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'variable'


class ViewsDataExport(models.Model):
    eid = models.AutoField(primary_key=True)
    view_name = models.CharField(max_length=32)
    view_display_id = models.CharField(max_length=32)
    time_stamp = models.PositiveIntegerField()
    fid = models.PositiveIntegerField()
    batch_state = models.CharField(max_length=32)
    sandbox = models.TextField()

    class Meta:
        managed = False
        db_table = 'views_data_export'


class ViewsDataExportObjectCache(models.Model):
    eid = models.CharField(max_length=64, blank=True, null=True)
    updated = models.PositiveIntegerField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'views_data_export_object_cache'


class ViewsDisplay(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    id = models.CharField(max_length=64)
    display_title = models.CharField(max_length=64)
    display_plugin = models.CharField(max_length=64)
    position = models.IntegerField(blank=True, null=True)
    display_options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'views_display'
        unique_together = (('vid', 'id'),)


class ViewsObjectCache(models.Model):
    sid = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    obj = models.CharField(max_length=32, blank=True, null=True)
    updated = models.PositiveIntegerField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'views_object_cache'


class ViewsView(models.Model):
    vid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=32)
    description = models.CharField(max_length=255, blank=True, null=True)
    tag = models.CharField(max_length=255, blank=True, null=True)
    base_table = models.CharField(max_length=64)
    core = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'views_view'


class Vocabulary(models.Model):
    vid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    help = models.CharField(max_length=255)
    relations = models.PositiveIntegerField()
    hierarchy = models.PositiveIntegerField()
    multiple = models.PositiveIntegerField()
    required = models.PositiveIntegerField()
    tags = models.PositiveIntegerField()
    module = models.CharField(max_length=255)
    weight = models.IntegerField()
    language = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'vocabulary'


class VocabularyNodeTypes(models.Model):
    vid = models.PositiveIntegerField()
    type = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'vocabulary_node_types'
        unique_together = (('type', 'vid'),)


class WorkflowAccess(models.Model):
    sid = models.AutoField()
    rid = models.IntegerField()
    grant_view = models.PositiveIntegerField()
    grant_update = models.PositiveIntegerField()
    grant_delete = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'workflow_access'


class WorkflowNode(models.Model):
    nid = models.PositiveIntegerField(primary_key=True)
    sid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    stamp = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'workflow_node'


class WorkflowNodeHistory(models.Model):
    hid = models.AutoField(primary_key=True)
    nid = models.PositiveIntegerField()
    old_sid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    stamp = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflow_node_history'


class WorkflowScheduledTransition(models.Model):
    nid = models.PositiveIntegerField()
    old_sid = models.PositiveIntegerField()
    sid = models.PositiveIntegerField()
    scheduled = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflow_scheduled_transition'


class WorkflowStates(models.Model):
    sid = models.AutoField(primary_key=True)
    wid = models.PositiveIntegerField()
    state = models.CharField(max_length=255)
    weight = models.IntegerField()
    sysid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'workflow_states'


class WorkflowTransitions(models.Model):
    tid = models.AutoField(primary_key=True)
    sid = models.PositiveIntegerField()
    target_sid = models.PositiveIntegerField()
    roles = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflow_transitions'


class WorkflowTypeMap(models.Model):
    type = models.CharField(max_length=255)
    wid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'workflow_type_map'


class Workflows(models.Model):
    wid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tab_roles = models.CharField(max_length=60)
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workflows'
