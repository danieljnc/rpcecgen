from django.http import HttpResponse
from django.template import loader

from apps.clinicalTrial.models import *


# Create your views here.
def generate_xml_with_template(request):
    clinical_trials = ContentTypeClinicalTrials.objects.filter(field_id_number_value__icontains="RPCEC").order_by(
        '-vid')
    rpcec = DatosInternosRpcec.objects.all()[0].cod_rpcec

    i = 1
    trial_list = []
    while i <= rpcec:
        j = i
        aux = 'RPCEC' + str(j).zfill(8)
        clinical_trial = clinical_trials.filter(field_id_number_value=aux)[0]
        trial_list.append(clinical_trial)
        i += 1

    print(len(trial_list))

    for trial in trial_list:
        # Formatting date of registration
        if int(trial.field_id_number_value[5:]) <= 163:
            date_registration = str(trial.field_date_register_value[-2:]) + '/' + str(
                trial.field_date_register_value[5:7]) + '/' + str(trial.field_date_register_value[0:4])

        else:
            date_registration = str(trial.field_date_register_value)

        trial.field_date_register_value = date_registration

        # Searching public title
        title = Node.objects.get(nid=trial.nid, type='clinical_trials')
        trial.public_title = title.title

        # Formatting date enrolment
        date_enrolment = str(trial.field_date_first_enrollment_value)[8:10] + '/' + str(
            trial.field_date_first_enrollment_value)[5:7] + '/' + str(trial.field_date_first_enrollment_value)[
                                                                  0:4]
        trial.field_date_first_enrollment_value = date_enrolment

        # Setting type of enrolment
        if date_enrolment[-4:] < date_registration[-4:]:
            trial.type_of_enrolment = "actual"
        else:
            if date_enrolment[-4:] > date_registration[-4:]:
                trial.type_of_enrolment = "anticipated"
            else:
                if date_enrolment[-7:-5] < date_registration[-7:-5]:
                    trial.type_of_enrolment = "actual"
                else:
                    if date_enrolment[-7:-5] > date_registration[-7:-5]:
                        trial.type_of_enrolment = "anticipated"
                    else:
                        if date_enrolment[:2] >= date_registration[:2]:
                            trial.type_of_enrolment = "anticipated"
                        else:
                            trial.type_of_enrolment = "actual"

        # Formatting results date complete
        if trial.field_results_date_value is not None:
            result_date_complete = trial.field_results_date_value[8:10] + '/' + trial.field_results_date_value[
                                                                                5:7] + '/' + trial.field_results_date_value[
                                                                                             0:4]
            trial.field_results_date_value = result_date_complete

        # Formatting results date first publication
        if trial.field_first_publication_value is not None:
            result_date_first_publication = trial.field_first_publication_value[
                                            8:10] + '/' + trial.field_first_publication_value[
                                                          5:7] + '/' + trial.field_first_publication_value[
                                                                       0:4]
            trial.field_first_publication_value = result_date_first_publication

        # REVISAR PORQUE ESTE DATO NO ESTA APARECIENDO
        phone_public = ContentFieldPublicPhone.objects.filter(nid=trial.nid, vid=trial.vid).first()
        trial.field_phone_public_value = phone_public.field_public_phone_number

        email_public = ContentFieldEmailPublic.objects.filter(nid=trial.nid, vid=trial.vid).first()
        trial.field_email_public_value = email_public.field_email_public_email

        phone_scientific = ContentFieldScientificPhone.objects.filter(nid=trial.nid, vid=trial.vid).first()
        trial.field_phone_scientific_value = phone_scientific.field_scientific_phone_number

        email_scientific = ContentFieldEmailScientific.objects.filter(nid=trial.nid, vid=trial.vid).first()
        trial.field_phone_scientific_value = email_scientific.field_email_scientific_email

        # BUSCAR EJEMPLO DE ENSAYO CON MAS DE UN PAIS
        trial.countries = ContentFieldCountries.objects.filter(nid=trial.nid, vid=trial.vid)

        trial.hc_codes = ContentFieldHcCode.objects.filter(nid=trial.nid, vid=trial.vid)

        # REVISAR PORQUE ESTE DATO NO ESTA APARECIENDO
        trial.hc_keywords = ContentFieldHcKeyword.objects.filter(nid=trial.nid, vid=trial.vid)

        trial.i_codes = ContentFieldInterCode.objects.filter(nid=trial.nid, vid=trial.vid)

        trial.secondary_sponsors = ContentFieldSecSponsor.objects.filter(nid=trial.nid, vid=trial.vid)

        sec_ids = ContentFieldIdentifying.objects.filter(nid=trial.nid, vid=trial.vid)

        issuing_authorities = ContentFieldAuthorityIdentifying.objects.filter(nid=trial.nid, vid=trial.vid)
        secondary_ids = []
        for i in range(0, len(sec_ids)):
            secondary_id = {'sec_id': sec_ids[i].field_identifying_value,
                            'issuing_authorities': issuing_authorities[i].field_authority_identifying_value}
            secondary_ids.append(secondary_id)

        trial.secondary_ids = secondary_ids

        ethics_reviews = ContentFieldResearchCommittee.objects.filter(nid=trial.nid, vid=trial.vid)

        ethics_committee = []
        for i in range(0, len(ethics_reviews)):
            ethic_committee = {}

            ethics_status = ContentFieldEvaluationStatus.objects.get(nid=trial.nid, vid=trial.vid, delta=ethics_reviews[i].delta)
            ethic_committee['status'] = ethics_status.field_evaluation_status_value
            
            approval_date = ContentFieldDateCommittee.objects.get(nid=trial.nid, vid=trial.vid, delta=ethics_reviews[i].delta)
            
            if approval_date.field_date_committee_value:
                ethic_committee['approval_date'] = approval_date.field_date_committee_value[8:10] + '/' + approval_date.field_date_committee_value[5:7] + '/' + approval_date.field_date_committee_value[0:4]
            else:
                ethic_committee['approval_date'] = None

            ethic_committee['contact_name'] = ethics_reviews[i].field_research_committee_value

            contact_address = ContentFieldZipCommittee.objects.get(nid=trial.nid, vid=trial.vid, delta=ethics_reviews[i].delta)
            ethic_committee['contact_address'] = contact_address.field_zip_committee_value

            try:
                contact_phone = ContentFieldCommmitteFhone.objects.get(nid=trial.nid, vid=trial.vid, delta=ethics_reviews[i].delta)
            except ContentFieldCommmitteFhone.DoesNotExist:
                contact_phone.field_commmitte_fhone_value = '-'

            ethic_committee['contact_phone'] = contact_phone.field_commmitte_fhone_value

            try:
                contact_email = ContentFieldCommmitteMail.objects.get(nid=trial.nid, vid=trial.vid, delta=ethics_reviews[i].delta)
            except ContentFieldCommmitteMail.DoesNotExist:
                contact_email.field_commmitte_mail_value = '-'
                
            ethic_committee['contact_email'] = contact_email.field_commmitte_mail_value

            ethics_committee.append(ethic_committee)        

        trial.ethics_committee = ethics_committee

    xml_template = loader.get_template('xml_template.xml')

    response = HttpResponse(xml_template.render({'trial_list': trial_list}), content_type="application/xml")
    response['Content-Disposition'] = 'attachment; filename=xml_template.xml'

    return response
