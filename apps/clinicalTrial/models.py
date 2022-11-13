from django.db import models


# Create your models here.

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

    def __str__(self):
        if self.field_id_number_value:
            return self.field_id_number_value
        else:
            return self.field_scientific_title_value


class DatosInternosRpcec(models.Model):
    cod_rpcec = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'datos_internos_rpcec'

    def __str__(self):
        return self.cod_rpcec


class ContentFieldEmailPublic(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_email_public_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_email_public'
        unique_together = (('vid', 'delta'),)

    def __str__(self):
        return self.field_email_public_email


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

    def __str__(self):
        return str(self.field_public_phone_number)


class ContentFieldEmailScientific(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_email_scientific_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_email_scientific'
        unique_together = (('vid', 'delta'),)

    def __str__(self):
        return self.field_email_scientific_email


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

    def __str__(self):
        return self.field_scientific_phone_number


class ContentFieldCountries(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_countries_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_countries'
        unique_together = (('vid', 'delta'),)

    def __str__(self):
        return self.field_countries_value


class ContentFieldHcCode(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_hc_code_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_hc_code'
        unique_together = (('vid', 'delta'),)

    def __str__(self):
        return self.field_hc_code_value


class ContentFieldHcKeyword(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_hc_keyword_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_hc_keyword'
        unique_together = (('vid', 'delta'),)

    def __str__(self):
        return self.field_hc_keyword_value


class ContentFieldInterCode(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_inter_code_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_inter_code'
        unique_together = (('vid', 'delta'),)

    def __str__(self):
        return self.field_inter_code_value


class ContentFieldSecSponsor(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_sec_sponsor_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_sec_sponsor'
        unique_together = (('vid', 'delta'),)


class ContentFieldIdentifying(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_identifying_value = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.field_identifying_value:
            return self.field_identifying_value
        return 'None'

    class Meta:
        managed = False
        db_table = 'content_field_identifying'
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


class ContentFieldResearchCommittee(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_research_committee_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_research_committee'
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


class ContentFieldDateCommittee(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_date_committee_value = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_date_committee'
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


class ContentFieldEmailInvestigator(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_email_investigator_email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_email_investigator'
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

    # def __str__(self):
    #     return self.field_investigator_phone_country_codes + self.field_investigator_phone_number


class ContentFieldParticipatingSc(models.Model):
    vid = models.PositiveIntegerField(primary_key=True)
    nid = models.PositiveIntegerField()
    delta = models.PositiveIntegerField()
    field_participating_sc_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content_field_participating_sc'
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
