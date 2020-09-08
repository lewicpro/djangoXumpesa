from django import forms
from .models import *
from app.models import *
from app.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime

class hireform(forms.ModelForm):
    user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'user', 'style': 'width: 100%;', 'class':"textinput textInput form-control " }))
    location_address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Location & Adress', 'style': 'width: 100%;', 'class':'textinput textInput form-control ' }))
    job_title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'job title', 'style': 'width: 100%; padding-top: 2px;', 'class':'textinput textInput form-control '}))
    employer_title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'employer_title', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    organization = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'organization', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    position_type = forms.ChoiceField(label='', choices=positiontyp, widget=forms.Select(attrs={'placeholder': 'position type', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'phone number', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    city_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'City', 'style': 'width: 100%', 'class':'textinput textInput form-control '}))
    Country_of_work = forms.ChoiceField(choices=COUNTRIES, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%;', 'class':'textinput textInput form-control '}), required=True)
    job_descriptions = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'job descriptions', 'style': 'width: 100%', 'class':'textinput text-center textInput form-control '}))
    specifications = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'specifications.. split specifications by comma(,)', 'style': 'width: 100%', 'class':'textinput text-center textInput form-control '}))
    application_deadline = forms.DateField(label='', widget=forms.DateInput(attrs={'type':'date', 'placeholder': 'application deadline', 'style': 'width: 100%', 'class':'textinput text-center textInput form-control '}))

    class Meta:
        model = Jobs
        fields = {
            'user',
            'full_name',
            'country',
            'location_address',
            'job_title',
            'Country_of_work',
            'position_type',
            'organization',
            'phone_number',
            'email',
            'employer_title',
            'job_descriptions',
            'specifications',
            'city_name',
            'application_deadline',

        }

    def clean_application_deadline(self):
        application_deadline = self.cleaned_data.get('application_deadline')
        if application_deadline < datetime.date.today():
            raise forms.ValidationError('The date you have filled has aready passed')




class Markform(forms.ModelForm):
    # user = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'user', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    # location_address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Location & Adress', 'style': 'width: 100%;','class': 'textinput textInput form-control '}))
    # job_title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'job title', 'style': 'width: 100%; padding-top: 2px;','class': 'textinput textInput form-control '}))
    # employer_title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'employer_title', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    # organization = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'organization', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    # position_type = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'position type', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    # phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'phone number', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    # email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    # city_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'City', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    # Country_of_work = forms.ChoiceField(choices=COUNTRIES, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    # job_descriptions = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'job descriptions', 'style': 'width: 100%','class': 'textinput text-center textInput form-control '}))
    # specifications = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'specifications.. split specifications by comma(,)', 'style': 'width: 100%','class': 'textinput text-center textInput form-control '}))
    # application_deadline = forms.DateField(label='', widget=forms.DateInput(attrs={'placeholder': 'application deadline', 'style': 'width: 100%','class': 'textinput textInput form-control '}))

    class Meta:
        model = Marked
        fields = {
            'user',
            'job_id',
            'full_name',
            'location_address',
            'job_title',
            'Country_of_work',
            'position_type',
            'organization',
            'phone_number',
            'email',
            'employer_title',
            'job_descriptions',
            'specifications',
            'city_name',
            'application_deadline',

        }



class AcceptedForm(forms.ModelForm):

    class Meta:
        model = AcceptedApp
        fields = {
            'user',
            'job_id',
            'full_name',
            'applier',
            'job_title',
            'Country_of_work',
            'country',
            'specifications',
            'city_name',
            'Descrip',
        }



class CV1form(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'first name', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    middle_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Middle name', 'style': 'width: 100%;','class': 'textinput textInput form-control '}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'last name', 'style': 'width: 100%; padding-top: 2px;','class': 'textinput textInput form-control '}))
    Gender = forms.ChoiceField(choices=gender, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    place_of_birth = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'place of birth', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    date_of_birth = forms.DateField(label='', widget=forms.DateInput(attrs={'placeholder': 'date of birth', 'type':'date', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    Marital_status = forms.ChoiceField(choices=marital, label="", initial='', widget=forms.Select(attrs={'placeholder': 'Marital status', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    criminal_record = forms.ChoiceField(choices=disability, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    years_of_work_experience = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Years of work experience', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    nationality = forms.ChoiceField(choices=COUNTRIES, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    disability = forms.ChoiceField(choices=disability, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)

    class Meta:
        model = CVpersonal
        fields = {
            "first_name",
            "middle_name",
            "last_name",
            "Gender",
            "place_of_birth",
            "date_of_birth",
            "Marital_status",
            "criminal_record",
            "years_of_work_experience",
            "nationality",
            "disability",

        }


class ContactForm(forms.ModelForm):
    present_address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'present address', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    permanent_address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'permanent_address', 'style': 'width: 100%;','class': 'textinput textInput form-control '}))
    Telephone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Telephone', 'style': 'width: 100%; padding-top: 2px;','class': 'textinput textInput form-control '}))
    work_telephone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Work telephone', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    country_of_residence = forms.ChoiceField(choices=COUNTRIES, label="", initial='', widget=forms.Select(attrs={'placeholder': 'Marital status', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    country_code = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Country code', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    mobile_no = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'mobile no', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))
    altenative_email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'altelnative email', 'style': 'width: 100%', 'class': 'textinput textInput form-control '}))

    class Meta:
        model = CVcontact
        fields = {
            "present_address",
            "permanent_address",
            "Telephone",
            "work_telephone",
            "country_of_residence",
            "country_code",
            "mobile_no",
            "altenative_email",
        }



class AcademicForm(forms.ModelForm):
    educational_level = forms.ChoiceField(choices=level, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    program_name= forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Program name', 'style': 'width: 100%;','class': 'textinput textInput form-control '}))
    institution_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Institution name', 'style': 'width: 100%; padding-top: 2px;','class': 'textinput textInput form-control '}))
    attach_certificate = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    country = forms.ChoiceField(choices=COUNTRIES, label="", initial='', widget=forms.Select(attrs={'placeholder': 'Country ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    start_time = forms.ChoiceField(choices=YEAR, label="", initial='', widget=forms.Select(attrs={'placeholder': 'Country ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    end_time = forms.ChoiceField(choices=YEAR, label="", initial='', widget=forms.Select(attrs={'placeholder': 'Country ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)

    class Meta:
        model = CVaccademic
        fields = {
              "educational_level",
              "country",
              "institution_name",
              "attach_certificate",
              "program_name",
              "start_time",
              "end_time"
        }



class ProffessionForm(forms.ModelForm):
    country_prof= forms.ChoiceField(choices=COUNTRIES, label="", initial='', widget=forms.Select(attrs={'placeholder': 'Country ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    institution_name_prof= forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'institution name', 'style': 'width: 100%;','class': 'textinput textInput form-control '}))
    course_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'course name', 'style': 'width: 100%; padding-top: 2px;','class': 'textinput textInput form-control '}))
    start_time_prof = forms.ChoiceField(choices=YEAR, label="", initial='', widget=forms.Select(attrs={'placeholder': 'Country ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    end_time_prof = forms.ChoiceField(choices=YEAR, label="", initial='', widget=forms.Select(attrs={'placeholder': 'Country ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    attach_certificate_prof = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))

    class Meta:
        model = CVprofession
        fields = [
            "country_prof",
            "institution_name_prof",
            "course_name",
            "start_time_prof",
            "end_time_prof",
            "attach_certificate_prof"
        ]



class LanguageForm(forms.ModelForm):
    language1 = forms.ChoiceField(choices=lang, label="", initial='', widget=forms.Select(attrs={'placeholder': ' ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    Quality1= forms.ChoiceField(choices=quality, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    language2 = forms.ChoiceField(choices=lang, label="", initial='', widget=forms.Select(attrs={'placeholder': ' ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    Quality2= forms.ChoiceField(choices=quality, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%', 'type':'radio', 'required':True }), )
    language3 = forms.ChoiceField(choices=lang, label="", initial='', widget=forms.Select(attrs={'placeholder': ' ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    Quality3 = forms.ChoiceField(choices=quality, label="", initial='', widget=forms.RadioSelect(attrs={'style': 'width: 100%; list-style-type: none;', 'type':'radio', 'required':True }), )

    class Meta:
        model = CVlanguage
        fields = [
              "language1",
              "Quality1",
              "language2",
              "Quality2",
              "language3",
              "Quality3",
            ]




class WorkForm(forms.ModelForm):
    organization = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'organization', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    supervisor_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'supervisor_name', 'style': 'width: 100%;','class': 'textinput textInput form-control '}))
    supervisor_address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'supervisor telephone number', 'style': 'width: 100%; padding-top: 2px;','class': 'textinput textInput form-control '}))
    supervisor_telephone_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'supervisor telephone number', 'style': 'width: 100%; padding-top: 2px;','class': 'textinput textInput form-control '}))
    job_title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'job title', 'style': 'width: 100%','class': 'textinput textInput form-control '}))
    Duties_and_responsibilities = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Duties and responsibilities', 'style': 'width: 100%','class': 'textinput textInput form-control '}))
    current_job = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'current job', 'style': 'width: 100%','class': 'textinput textInput form-control '}))
    start_date = forms.ChoiceField(choices=YEAR, label="", initial='', widget=forms.Select(attrs={'placeholder': '', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    end_date = forms.ChoiceField(choices=YEAR, label="", initial='', widget=forms.Select(attrs={'placeholder': ' ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    class Meta:
        model = CVwork
        fields = [
              "organization",
              "supervisor_name",
              "supervisor_telephone_number",
              "job_title",
              "supervisor_address",
              "Duties_and_responsibilities",
              "start_date",
              "current_job",
              "end_date"
            ]



class TrainingForm(forms.ModelForm):
    training_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'training_name', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    Institution = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Institution', 'style': 'width: 100%;','class': 'textinput textInput form-control '}))
    Attact_your_certificate = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': '', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    description_training = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'description training', 'style': 'width: 100%; padding-top: 2px;','class': 'textinput textInput form-control '}))
    starting_date_teraining = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'starting date', 'style': 'width: 100%','class': 'textinput textInput form-control '}))
    end_date_teraining = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'end date', 'style': 'width: 100%','class': 'textinput textInput form-control '}))
    class Meta:
        model = CVtraining
        fields  = [
            "training_name",
            "Institution",
            "Attact_your_certificate",
            "description_training",
            "starting_date_teraining",
            "end_date_teraining"
        ]




class ComputerForm(forms.ModelForm):
    computer_skills = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'computer skills', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    quality_computer = forms.ChoiceField(choices=quality, label="", initial='', widget=forms.Select(attrs={'placeholder': 'Country ', 'style': 'width: 100%; padding-bottom: 3%'}), required=True)
    attach_certificate_train = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    class Meta:
        model = CVcomputer
        fields  = [
            "computer_skills",
            "quality_computer",
            "attach_certificate_train"
        ]





class RefreeForm(forms.ModelForm):
    referee_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'referee name', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    organisation_of_a_referee = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'organisation of a referee', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'title', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    referee_email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'referee email', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    referee_address = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'referee address', 'style': 'width: 100%;', 'class': "textinput textInput form-control "}))
    other_certificates1 = forms.FileField(label=' ', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    other_certificates2 = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    other_certificates3 = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    other_certificates4 = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    TCU_certificate = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    recomendation_letter = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    birth_certificate = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    CV = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))
    other_attachment1 = forms.FileField(label='', widget=forms.FileInput(attrs={'placeholder': 'attach certificate train', 'type':'file', 'style': 'width: 100%; padding-top: 2px;','class': 'fa-file-pdf-0'}))

    class Meta:
        model = CVrefree
        fields = [
            "referee_name",
            "organisation_of_a_referee",
            "title",
            "referee_email",
            "referee_address",
            "other_attachment1",
            "CV",
            "birth_certificate",
            "recomendation_letter",
            "TCU_certificate",
            "other_certificates1",
            "other_certificates2",
            "other_certificates3",
            "other_certificates4"
        ]


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = {
            'job_id',
            'country',
            'acc_owner',
            'city_name',
            'job_title',
            'Country_of_work',
            'location_address',
            'specifications',
            'position_type',
            'organization',
            'posted',
            'application_deadline',
            'user_id',
            'user',
            'full_name_xampesa',
            'first_name_per',
            'middle_name_per',
            'last_name_per',
            'Gender_per',
            'place_of_birth_per',
            'date_of_birth_per',
            'Marital_status_per',
            'criminal_record_per',
            'years_of_work_experience_per',
            'nationality_per',
            'disability_per',
            'present_address_con',
            'permanent_address_con',
            'work_telephone_con',
            'country_of_residence_con',
            'Telephone_con',
            'country_code_con',
            'mobile_no_con',
            'altenative_email_con',
            'educational_level_aca',
            'country_aca',
            'institution_name_aca',
            'attach_certificate_aca',
            'program_name_aca',
            'start_time_aca',
            'end_time_aca',
            'country_prof',
            'institution_name_prof',
            'course_name_prof',
            'start_time_prof',
            'end_time_prof',
            'attach_certificate_prof',
            'language1',
            'quality1',
            'language2',
            'quality2',
            'language3',
            'quality3',
            'organization_wor',
            'job_title_wor',
            'supervisor_name_wor',
            'supervisor_telephone_number_wor',
            'supervisor_address_wor',
            'Duties_and_responsibilities_wor',
            'current_job_wor',
            'start_date_wor',
            'end_date_wor',
            'training_name',
            'Institution',
            'Attact_your_certificate',
            'description_training',
            'starting_date_teraining',
            'end_date_teraining',
            'computer_skills',
            'quality_computer',
            'attach_certificate_train',
            'referee_name',
            'organisation_of_a_referee',
            'title',
            'referee_email',
            'referee_address',
            'other_attachment1',
            'birth_certificate',
            'recomendation_letter',
            'TCU_certificate',
            'other_certificates1',
            'other_certificates2',
            'other_certificates3',
            'other_certificates4',
            'CV'

        }