from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from .forms import TrialFiltersForm


# Create your views here.
def homepage(request):
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

    context = {'trial_registrered': len(trial_list)}
    trial_anticipated = 0
    trial_actual = 0

    trial_year = {'trial_january': 0, 'trial_february': 0, 'trial_march': 0, 'trial_april': 0, 'trial_may': 0,
                  'trial_june': 0, 'trial_july': 0, 'trial_august': 0, 'trial_september': 0, 'trial_october': 0,
                  'trial_november': 0, 'trial_december': 0}

    for trial in trial_list:
        # Formatting date of registration
        if int(trial.field_id_number_value[5:]) <= 163:
            date_registration = str(trial.field_date_register_value[-2:]) + '/' + str(
                trial.field_date_register_value[5:7]) + '/' + str(trial.field_date_register_value[0:4])

        else:
            date_registration = str(trial.field_date_register_value)

        if date_registration[-4:] == '2021':
            if date_registration[-7:-5] == '01':
                trial_year['trial_january'] = trial_year['trial_january'] + 1

            if date_registration[-7:-5] == '02':
                trial_year['trial_february'] = trial_year['trial_february'] + 1

            if date_registration[-7:-5] == '03':
                trial_year['trial_march'] = trial_year['trial_march'] + 1

            if date_registration[-7:-5] == '04':
                trial_year['trial_april'] = trial_year['trial_april'] + 1

            if date_registration[-7:-5] == '05':
                trial_year['trial_may'] = trial_year['trial_may'] + 1

            if date_registration[-7:-5] == '06':
                trial_year['trial_june'] = trial_year['trial_june'] + 1

            if date_registration[-7:-5] == '07':
                trial_year['trial_july'] = trial_year['trial_july'] + 1

            if date_registration[-7:-5] == '08':
                trial_year['trial_august'] = trial_year['trial_august'] + 1

            if date_registration[-7:-5] == '09':
                trial_year['trial_september'] = trial_year['trial_september'] + 1

            if date_registration[-7:-5] == '10':
                trial_year['trial_october'] = trial_year['trial_october'] + 1

            if date_registration[-7:-5] == '11':
                trial_year['trial_november'] = trial_year['trial_november'] + 1

            if date_registration[-7:-5] == '12':
                trial_year['trial_december'] = trial_year['trial_december'] + 1

        # Formatting date enrolment
        date_enrolment = str(trial.field_date_first_enrollment_value)[8:10] + '/' + str(
            trial.field_date_first_enrollment_value)[5:7] + '/' + str(trial.field_date_first_enrollment_value)[
                                                                  0:4]
        # Setting type of enrolment
        if date_enrolment[-4:] < date_registration[-4:]:
            trial_actual = trial_actual + 1
        else:
            if date_enrolment[-4:] > date_registration[-4:]:
                trial_anticipated = trial_anticipated + 1
            else:
                if date_enrolment[-7:-5] < date_registration[-7:-5]:
                    trial_actual = trial_actual + 1
                else:
                    if date_enrolment[-7:-5] > date_registration[-7:-5]:
                        trial_anticipated = trial_anticipated + 1
                    else:
                        if date_enrolment[:2] >= date_registration[:2]:
                            trial_anticipated = trial_anticipated + 1
                        else:
                            trial_actual = trial_actual + 1

    context['trial_anticipated'] = trial_anticipated
    context['trial_actual'] = trial_actual
    context['trial_year'] = list(trial_year.values())

    return render(request, 'index.html', context)


class ClinicalTrialListView(ListView):
    model = ContentTypeClinicalTrials
    template_name = 'clinical_trial/clinical_trial_list.html'
    context_object_name = 'ClinicalTrials'

    def get_queryset(self):
        clinical_trials = ContentTypeClinicalTrials.objects.filter(field_id_number_value__icontains="RPCEC").order_by(
            '-vid')
        rpcec = DatosInternosRpcec.objects.all()[0].cod_rpcec

        i = 1
        trial_list = []

        recruitment_status = self.request.GET.get('recruitment_status_field')
        if recruitment_status:
            clinical_trials = clinical_trials.filter(field_recruitment_status_value=recruitment_status)

        phase = self.request.GET.get('phase_field')
        if phase:
            clinical_trials = clinical_trials.filter(field_phase_value=phase)

        covid_trial = self.request.GET.get('covid_trial_field')
        if covid_trial == "1":
            clinical_trials = clinical_trials.filter(field_scientific_title_value__icontains='COVID-19')

        while i <= rpcec:
            j = i
            aux = 'RPCEC' + str(j).zfill(8)
            try:
                clinical_trial = clinical_trials.filter(field_id_number_value=aux)[0]
                trial_list.append(clinical_trial)
            except:
                pass
            i += 1

        return trial_list

    def get_context_data(self, **kwargs):
        context = super(ClinicalTrialListView, self).get_context_data(**kwargs)
        context['form'] = TrialFiltersForm(initial={
            'recruitment_status_field': self.request.GET.get('recruitment_status_field'),
            'phase_field': self.request.GET.get('phase_field'),
            'covid_trial_field': self.request.GET.get('covid_trial_field'),
        })
        return context


class ClinicalTrialDetailView(DetailView):
    model = ContentTypeClinicalTrials
    template_name = 'clinical_trial/clinical_trial_detail.html'
    context_object_name = 'trial'

    def get_context_data(self, **kwargs):
        context = super(ClinicalTrialDetailView, self).get_context_data(**kwargs)

        context['object'].secondary_sponsors = ContentFieldSecSponsor.objects.filter(nid=context['object'].nid,
                                                                                     vid=context['object'].vid)

        sec_ids = ContentFieldIdentifying.objects.filter(nid=context['object'].nid, vid=context['object'].vid)

        issuing_authorities = ContentFieldAuthorityIdentifying.objects.filter(nid=context['object'].nid,
                                                                              vid=context['object'].vid)
        secondary_ids = []
        for i in range(0, len(sec_ids)):
            secondary_id = {'sec_id': sec_ids[i].field_identifying_value,
                            'issuing_authorities': issuing_authorities[i].field_authority_identifying_value}
            secondary_ids.append(secondary_id)

        context['object'].secondary_ids = secondary_ids

        context['object'].principal_investigator_phone = ContentFieldInvestigatorPhone.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid)

        context['object'].principal_investigator_email = ContentFieldEmailInvestigator.objects.filter(
            nid=context['object'].nid,
            vid=context['object'].vid)

        context['object'].countries = ContentFieldCountries.objects.filter(
            nid=context['object'].nid, vid=context['object'].vid)

        context['object'].clinical_sites = ContentFieldParticipatingSc.objects.filter(
            nid=context['object'].nid, vid=context['object'].vid)

        context['object'].ethics_committes = ContentFieldEthicsCommittes.objects.filter(
            nid=context['object'].nid, vid=context['object'].vid)

        context['object'].hc_codes = ContentFieldHcCode.objects.filter(
            nid=context['object'].nid, vid=context['object'].vid)

        context['object'].hc_keywords = ContentFieldHcKeyword.objects.filter(
            nid=context['object'].nid, vid=context['object'].vid)

        context['object'].i_codes = ContentFieldInterCode.objects.filter(
            nid=context['object'].nid, vid=context['object'].vid)

        context['object'].field_phone_public_value = ContentFieldPublicPhone.objects.filter(
            nid=context['object'].nid, vid=context['object'].vid)

        context['object'].field_email_public_value = ContentFieldEmailPublic.objects.filter(
            nid=context['object'].nid, vid=context['object'].vid)

        context['object'].field_phone_scientific_value = ContentFieldScientificPhone.objects.filter(
            nid=context['object'].nid, vid=context['object'].vid)

        context['object'].field_phone_scientific_value = ContentFieldEmailScientific.objects.filter(
            nid=context['object'].nid, vid=context['object'].vid)

        if context['object'].field_study_date_value:
            context['object'].field_study_date_value = str(context['object'].field_study_date_value[8:10]) + '/' + str(
                context['object'].field_study_date_value[5:7]) + '/' + str(
                context['object'].field_study_date_value[0:4])

        if context['object'].field_results_date_value:
            context['object'].field_results_date_value = str(
                context['object'].field_results_date_value[8:10]) + '/' + str(
                context['object'].field_results_date_value[5:7]) + '/' + str(
                context['object'].field_results_date_value[0:4])

        if context['object'].field_first_publication_value:
            context['object'].field_first_publication_value = str(
                context['object'].field_first_publication_value[8:10]) + '/' + str(
                context['object'].field_first_publication_value[5:7]) + '/' + str(
                context['object'].field_first_publication_value[0:4])

        ethics_reviews = ContentFieldResearchCommittee.objects.filter(nid=context['object'].nid,
                                                                      vid=context['object'].vid)

        ethics_committee = []
        for i in range(0, len(ethics_reviews)):
            ethic_committee = {}

            ethic_committee['name'] = ethics_reviews[i].field_research_committee_value
            ethics_status = ContentFieldEvaluationStatus.objects.get(nid=context['object'].nid,
                                                                     vid=context['object'].vid,
                                                                     delta=ethics_reviews[i].delta)
            ethic_committee['status'] = ethics_status.field_evaluation_status_value

            approval_date = ContentFieldDateCommittee.objects.get(nid=context['object'].nid, vid=context['object'].vid,
                                                                  delta=ethics_reviews[i].delta)
            if approval_date.field_date_committee_value:
                ethic_committee['approval_date'] = approval_date.field_date_committee_value[
                                                   8:10] + '/' + approval_date.field_date_committee_value[
                                                                 5:7] + '/' + approval_date.field_date_committee_value[
                                                                              0:4]
            else:
                ethic_committee['approval_date'] = None

            contact_address = ContentFieldZipCommittee.objects.get(nid=context['object'].nid, vid=context['object'].vid,
                                                                   delta=ethics_reviews[i].delta)
            ethic_committee['contact_address'] = contact_address.field_zip_committee_value

            try:
                contact_phone = ContentFieldCommmitteFhone.objects.get(nid=context['object'].nid,
                                                                       vid=context['object'].vid,
                                                                       delta=ethics_reviews[i].delta)
            except ContentFieldCommmitteFhone.DoesNotExist:
                contact_phone.field_commmitte_fhone_value = '-'

            ethic_committee['contact_phone'] = contact_phone.field_commmitte_fhone_value

            try:
                contact_email = ContentFieldCommmitteMail.objects.get(nid=context['object'].nid,
                                                                      vid=context['object'].vid,
                                                                      delta=ethics_reviews[i].delta)
            except ContentFieldCommmitteMail.DoesNotExist:
                contact_email.field_commmitte_mail_value = '-'

            ethic_committee['contact_email'] = contact_email.field_commmitte_mail_value

            ethics_committee.append(ethic_committee)

        context['object'].ethics_committee = ethics_committee
        return context
