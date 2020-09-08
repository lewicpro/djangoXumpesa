from django.db import models
import time, datetime
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import string
from django.utils import timezone
from django.conf import settings
import schedule
import random, string
from app.models import *
from market.models import *
from django.db.models.signals import post_save
from django.urls import reverse
from django.db.models import signals
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail




PartTime = 'Part time'
Fulltime = 'Full time'
positiontyp = (
    (Fulltime, 'Full time'),
    (PartTime, 'Part time'),
)


class Jobs(models.Model):
    full_name = models.CharField(max_length=120, blank=True, null=True)
    user = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    city_name = models.CharField(max_length=120, blank=True, null=True)
    job_title = models.CharField(max_length=120, blank=True, null=True)
    Country_of_work = models.CharField(max_length=120, choices=COUNTRIES, null=True)
    location_address = models.CharField(max_length=120, blank=True, null=True)
    position_type = models.CharField(max_length=120, blank=True, null=True, choices=positiontyp)
    organization = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=120, blank=True, null=True)
    specifications = models.TextField(max_length=120, blank=True, null=True)
    email = models.EmailField(max_length=120, blank=True, null=True)
    employer_title = models.CharField(max_length=120, blank=True, null=True)
    job_descriptions = models.TextField(max_length=120, blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    application_deadline = models.DateField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.user

    def get_job_descriptions(self):
        return self.job_descriptions.split(",")


    def get_job_specifications(self):
        return self.specifications.split(",")


class Marked(models.Model):
    job_id = models.CharField(max_length=120, blank=True, null=True)
    full_name = models.CharField(max_length=120, blank=True, null=True)
    user = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    city_name = models.CharField(max_length=120, blank=True, null=True)
    job_title = models.CharField(max_length=120, blank=True, null=True)
    Country_of_work = models.CharField(max_length=120, null=True)
    location_address = models.CharField(max_length=120, blank=True, null=True)
    position_type = models.CharField(max_length=120, blank=True, null=True)
    organization = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=120, blank=True, null=True)
    specifications = models.TextField(max_length=120, blank=True, null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    employer_title = models.CharField(max_length=120, blank=True, null=True)
    job_descriptions = models.TextField(max_length=400, blank=True, null=True)
    posted_date = models.CharField(max_length=120, blank=False, null=True)
    application_deadline = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.full_name

MALE = 'MALE'
FEMALE = 'FEMALE'
gender = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
)


single = 'Single'
married = 'Married'
marital = (
    (single, 'Single'),
    (married, 'Married'),
)

No = 'No'
Yes = 'Yes'
disability = (
    (No, 'No'),
    (Yes, 'Yes'),
)

VGood = 'Very Good'
Good = 'Good'
Bad = 'Bad'
quality = (
    (VGood , 'Very Good'),
    (Good, 'Good'),
    (Bad, 'Bad'),
)


English = 'English'
Swahili = 'Swahili'
French = 'French'
German = 'German'
Latin = 'Latin'
none = 'None'
lang = (
    (English , 'English'),
    (Swahili, 'Swahili'),
    (French, 'French'),
    (German, 'German'),
    (Latin, 'Latin'),
    (none, 'None'),
)


AD = 'Advanced diploma'
ACSE = 'Advanced Level (ACSE)'
Certificate = 'Certificate'
Degree = 'Degree '
Diploma = 'Diploma'
Master = 'Master'
OL = 'Ordinary level (CSE)'
PHD = 'PHD'
PGD = 'Post Graduate Diploma'
level = (
    (AD, 'Advanced diploma'),
    (ACSE, 'Advanced Level (ACSE)'),
    (Certificate, 'Certificate'),
    (Degree, 'Degree '),
    (Diploma, 'Diploma'),
    (Master, 'Master'),
    (OL, 'Ordinary level (CSE)'),
    (PHD, 'PHD'),
    (PGD, 'Post Graduate Diploma'),
)

Processing = 'Processing'
Accepted = 'Accepted'
status = (
    (Processing, 'Processing'),
    (Accepted, 'Accepted'),
)

Unread = 'Unread'
read = 'read'
pub = (
    (Unread, 'Unread'),
    (read, 'read'),
)


class Application(models.Model):
    user_id = models.CharField(max_length=120, blank=True, null=True)
    user = models.CharField(max_length=120, blank=True, null=True)
    full_name_xampesa = models.CharField(max_length=120, blank=True, null=True)
    acc_owner = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(max_length=120, choices=status, blank=True, default='Processing')
    #job
    job_id = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    city_name = models.CharField(max_length=120, blank=True, null=True)
    job_title = models.CharField(max_length=120, blank=True, null=True)
    Country_of_work = models.CharField(max_length=120, blank=True, null=True)
    location_address = models.CharField(max_length=120, blank=True, null=True)
    specifications = models.TextField(max_length=120, blank=True, null=True)
    position_type = models.CharField(max_length=120, blank=True, null=True)
    organization = models.CharField(max_length=120, blank=True, null=True)
    posted = models.CharField(max_length=120, blank=True, null=True)
    application_deadline = models.CharField(max_length=120, blank=True, null=True)
    # #personal details
    applied_on = models.DateField( auto_now_add=True, blank=False, null=True)
    first_name_per = models.CharField(max_length=120, blank=True, null=True)
    middle_name_per = models.CharField(max_length=120, blank=True, null=True)
    last_name_per = models.CharField(max_length=120, blank=True, null=True)
    Gender_per = models.CharField(max_length=120, blank=True, null=True)
    place_of_birth_per = models.CharField(max_length=120, blank=True, null=True)
    date_of_birth_per = models.CharField(max_length=120, blank=True, null=True)
    Marital_status_per = models.CharField(max_length=120, blank=True, null=True)
    criminal_record_per = models.CharField(max_length=120, blank=True, null=True)
    years_of_work_experience_per = models.CharField(max_length=120, blank=True, null=True)
    nationality_per = models.CharField(max_length=120, blank=True, null=True)
    disability_per = models.CharField(max_length=120, blank=True, null=True)
    #contact details
    present_address_con = models.CharField(max_length=120, blank=True, null=True)
    permanent_address_con = models.CharField(max_length=120, blank=True, null=True)
    Telephone_con = models.CharField(max_length=120, blank=True, null=True)
    work_telephone_con = models.CharField(max_length=120, blank=True, null=True)
    country_of_residence_con = models.CharField(max_length=120, blank=True, null=True)
    country_code_con = models.CharField(max_length=120, blank=True, null=True)
    mobile_no_con = models.CharField(max_length=120, blank=True, null=True)
    altenative_email_con = models.CharField(max_length=120, blank=True, null=True)
    #academic qualifications
    educational_level_aca = models.CharField(max_length=120, blank=True, null=True)
    country_aca = models.CharField(max_length=120, blank=True, null=True)
    institution_name_aca = models.CharField(max_length=120, blank=True, null=True)
    attach_certificate_aca = models.CharField(max_length=120, blank=True, null=True)
    program_name_aca = models.CharField(max_length=120, blank=True, null=True)
    start_time_aca = models.CharField(max_length=120, blank=True,  null=True)
    end_time_aca = models.CharField(max_length=120, blank=True, null=True)
    # proffession qualifications
    country_prof = models.CharField(max_length=120, blank=True,  null=True)
    institution_name_prof = models.CharField(max_length=120, blank=True, null=True)
    course_name_prof = models.CharField(max_length=120, blank=True, null=True)
    start_time_prof = models.CharField(max_length=120, blank=True,  null=True)
    end_time_prof = models.CharField(max_length=120, blank=True,  null=True)
    attach_certificate_prof = models.CharField(max_length=120, blank=True, null=True)
    #language proficiency
    language1 = models.CharField(max_length=120, blank=True, null=True)
    quality1 = models.CharField(max_length=120, blank=True, null=True)
    language2 = models.CharField(max_length=120, blank=True, null=True)
    quality2 = models.CharField(max_length=120, blank=True,  null=True)
    language3 = models.CharField(max_length=120, blank=True, null=True)
    quality3 = models.CharField(max_length=120, blank=True,  null=True)
    #work experimence
    organization_wor = models.CharField(max_length=120, blank=True, null=True)
    job_title_wor = models.CharField(max_length=120, blank=True, null=True)
    supervisor_name_wor = models.CharField(max_length=120, blank=True, null=True)
    supervisor_telephone_number_wor = models.CharField(max_length=120, blank=True, null=True)
    supervisor_address_wor = models.CharField(max_length=120, blank=True, null=True)
    Duties_and_responsibilities_wor = models.CharField(max_length=120, blank=True, null=True)
    start_date_wor = models.CharField(max_length=120, choices=YEAR, blank=True, null=True)
    current_job_wor = models.CharField(max_length=120, blank=True, null=True)
    end_date_wor = models.CharField(max_length=120, blank=True, null=True)
    #Training & Workshops Attended
    training_name = models.CharField(max_length=120, blank=True, null=True)
    Institution = models.CharField(max_length=120, blank=True, null=True)
    Attact_your_certificate = models.CharField(max_length=120, blank=True, null=True)
    description_training = models.CharField(max_length=120, blank=True, null=True)
    starting_date_teraining = models.CharField(max_length=120, blank=True, null=True)
    end_date_teraining = models.CharField(max_length=120, blank=True, null=True)
    #Computer Literacy
    computer_skills = models.CharField(max_length=120, blank=True, null=True)
    quality_computer = models.CharField(max_length=120, blank=True, null=True)
    attach_certificate_train = models.CharField(max_length=120, blank=True, null=True)
    #Referee
    referee_name = models.CharField(max_length=120, blank=True, null=True)
    organisation_of_a_referee = models.CharField(max_length=120, blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    referee_email = models.CharField(max_length=120, blank=True, null=True)
    referee_address = models.CharField(max_length=120, blank=True, null=True)
    other_attachment1 = models.CharField(max_length=120, blank=True, null=True)
    CV = models.CharField(max_length=120, blank=True, null=True)
    birth_certificate = models.CharField(max_length=120, blank=True, null=True)
    recomendation_letter = models.CharField(max_length=120, blank=True, null=True)
    TCU_certificate = models.CharField(max_length=120, blank=True, null=True)
    other_certificates1 = models.CharField(max_length=120, blank=True, null=True)
    other_certificates2 = models.CharField(max_length=120, blank=True, null=True)
    other_certificates3 = models.CharField(max_length=120, blank=True, null=True)
    other_certificates4 = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = "Applications of job"



class AcceptedApp(models.Model):
    job_id = models.CharField(max_length=120, blank=True, null=True)
    full_name = models.CharField(max_length=120, blank=True, null=True)
    user = models.CharField(max_length=120, blank=True, null=True)
    applier = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    reade = models.CharField(max_length=120, choices=pub, blank=True, default='Unread')
    city_name = models.CharField(max_length=120, blank=True, null=True)
    job_title = models.CharField(max_length=120, blank=True, null=True)
    Country_of_work = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    specifications = models.TextField(max_length=400, blank=True, null=True)
    Descrip = models.TextField(max_length=500, blank=True, null=True)



class CVpersonal(models.Model):
    #personal details
    user = models.OneToOneField(User, null=True)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    middle_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    Gender = models.CharField(max_length=120, blank=True, choices=gender, null=True)
    place_of_birth = models.CharField(max_length=120, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    Marital_status = models.CharField(max_length=120, blank=True, choices=marital, null=True)
    criminal_record = models.CharField(max_length=120, blank=True, choices=disability, null=True)
    years_of_work_experience = models.CharField(max_length=120, blank=True, null=True)
    nationality = models.CharField(max_length=120, blank=True, choices=COUNTRIES, null=True)
    disability = models.CharField(max_length=120, blank=True, choices=disability, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Personal details"


    #contact details
class CVcontact(models.Model):
    user = models.OneToOneField(User, null=True)
    present_address = models.CharField(max_length=120, blank=True, null=True)
    permanent_address = models.CharField(max_length=120, blank=True, null=True)
    Telephone = models.CharField(max_length=120, blank=True, null=True)
    work_telephone = models.CharField(max_length=120, blank=True, null=True)
    country_of_residence = models.CharField(max_length=120, blank=True, choices=COUNTRIES, null=True)
    country_code = models.CharField(max_length=120, blank=True, null=True)
    mobile_no = models.CharField(max_length=120, blank=True, null=True)
    altenative_email = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Contact details"


    #academic qualifications
class CVaccademic(models.Model):
    user = models.OneToOneField(User, null=True)
    educational_level = models.CharField(max_length=120, blank=True, choices=level, null=True)
    country = models.CharField(max_length=120, blank=True, choices=COUNTRIES, null=True)
    institution_name = models.CharField(max_length=120, blank=True,  null=True)
    attach_certificate = models.FileField(blank=True, null=True)
    program_name = models.FileField(blank=True, null=True)
    start_time = models.CharField(max_length=120, blank=True, choices=YEAR, null=True)
    end_time = models.CharField(max_length=120, blank=True, choices=YEAR, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Accademic qualifications"


    # proffession qualifications
class CVprofession(models.Model):
    user = models.OneToOneField(User, null=True)
    country_prof = models.CharField(max_length=120, blank=True, choices=COUNTRIES, null=True)
    institution_name_prof = models.CharField(max_length=120, blank=True, null=True)
    course_name = models.CharField(max_length=120, blank=True, null=True)
    start_time_prof = models.CharField(max_length=120, blank=True, choices=YEAR, null=True)
    end_time_prof = models.CharField(max_length=120, blank=True, choices=YEAR, null=True)
    attach_certificate_prof = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Profession qualifications"


    #language proficiency
class CVlanguage(models.Model):
    user = models.OneToOneField(User, null=True)
    language1 = models.CharField(max_length=120, choices=lang, blank=True, null=True)
    Quality1 = models.CharField(max_length=120, choices=quality, blank=True, null=True)
    language2 = models.CharField(max_length=120, choices=lang, blank=True, null=True)
    Quality2 = models.CharField(max_length=120, choices=quality, blank=True, null=True)
    language3 = models.CharField(max_length=120, choices=lang, blank=True, null=True)
    Quality3 = models.CharField(max_length=120, choices=quality, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "language profficiency"

    #work experiment
class CVwork(models.Model):
    user = models.OneToOneField(User, null=True)
    organization = models.CharField(max_length=120, blank=True, null=True)
    job_title = models.CharField(max_length=120, blank=True, null=True)
    supervisor_name = models.CharField(max_length=120, blank=True, null=True)
    supervisor_telephone_number = models.CharField(max_length=120, blank=True, null=True)
    supervisor_address = models.CharField(max_length=120, blank=True, null=True)
    Duties_and_responsibilities = models.CharField(max_length=120, blank=True, null=True)
    start_date = models.CharField(max_length=120, choices=YEAR, blank=True, null=True)
    current_job = models.CharField(max_length=120, blank=True, null=True)
    end_date = models.CharField(max_length=120, choices=YEAR, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Work experience"

    #Training & Workshops Attended
class CVtraining(models.Model):
    user = models.OneToOneField(User, null=True)
    training_name = models.CharField(max_length=120, blank=True, null=True)
    Institution = models.CharField(max_length=120, blank=True, null=True)
    Attact_your_certificate = models.CharField(max_length=120, blank=True, null=True)
    description_training = models.CharField(max_length=120, blank=True, null=True)
    starting_date_teraining = models.CharField(max_length=120, blank=True, null=True)
    end_date_teraining = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Trainings and Workshops"


    #Computer Literacy
class CVcomputer(models.Model):
    user = models.OneToOneField(User, null=True)
    computer_skills = models.CharField(max_length=120, blank=True, null=True)
    quality_computer = models.CharField(max_length=120, blank=True, choices=quality, null=True)
    attach_certificate_train = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Computer literacy"


    # Referee
class CVrefree(models.Model):
    user = models.OneToOneField(User, null=True)
    referee_name = models.CharField(max_length=120, blank=True, null=True)
    organisation_of_a_referee = models.CharField(max_length=120, blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    referee_email = models.EmailField(max_length=120, blank=True, null=True)
    referee_address = models.CharField(max_length=120, blank=True, null=True)
    other_attachment1 = models.FileField(blank=True, null=True)
    CV = models.FileField(blank=True, null=True)
    birth_certificate = models.FileField(blank=True, null=True)
    recomendation_letter = models.FileField(blank=True, null=True)
    TCU_certificate = models.FileField(blank=True, null=True)
    other_certificates1 = models.FileField(blank=True, null=True)
    other_certificates2 = models.FileField(blank=True, null=True)
    other_certificates3 = models.FileField(blank=True, null=True)
    other_certificates4 = models.FileField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name_plural = "Referee informations"

#
# def create_profile(sender, **kwargs):
#     user = kwargs["instance"]
#     if kwargs['created']:
#         user_profile = CVpersonal(user=user)
#         user_profile.save()
#         # invest = Investment(user=user)
#         # invest.save()
#         # cash = Deposits(user=user)
#         # cash.save()

post_save.connect(create_profile, sender=User)
