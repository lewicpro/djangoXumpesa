
from django.contrib import admin

from .models import *



def Processing (Modeladmin, request, queryset):
    queryset.update(status='Processing')


def Accepted(modeladmin, request, queryset):
    queryset.update(status='Accepted')


class JobsAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "location_address", "position_type", "job_title", "city_name", "country", "organization", "application_deadline",
                    "employer_title", "phone_number", "email"]


class MarkAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name", "location_address", "job_id", "position_type", "job_title", "city_name", "country", "organization", "application_deadline",
                    "employer_title", "phone_number", "email"]


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["user", "full_name_xampesa","acc_owner", "first_name_per", "middle_name_per", "last_name_per", "Gender_per", "place_of_birth_per", "date_of_birth_per", "Marital_status_per", "criminal_record_per", "years_of_work_experience_per",
                    "nationality_per", "disability_per", "status"]
    actions = [Processing, Accepted]

class CVpersonalAdmin(admin.ModelAdmin):
    list_display = ["user", "first_name", "middle_name", "last_name", "Gender", "place_of_birth", "date_of_birth", "Marital_status", "criminal_record", "years_of_work_experience",
                    "nationality", "disability"]



class CVcontactAdmin(admin.ModelAdmin):
    list_display = ["user", "present_address", "Telephone", "work_telephone", "country_code", "country_of_residence", "mobile_no", "altenative_email"]


class CVcomputerAdmin(admin.ModelAdmin):
    list_display = ["user", "computer_skills", "quality_computer", "attach_certificate_train" ]



class CVaccademicAdmin(admin.ModelAdmin):
    list_display = ["user", "educational_level", "country", "institution_name", "attach_certificate", "program_name", "start_time", "end_time"]



class CVprofessionAdmin(admin.ModelAdmin):
    list_display = ["user", "country_prof", "institution_name_prof", "course_name", "start_time_prof", "end_time_prof", "attach_certificate_prof"]



class CVlanguageAdmin(admin.ModelAdmin):
    list_display = ["user", "language1", "Quality1", "language2", "Quality2", "language3", "Quality3"]



class AcceptedAppAdmin(admin.ModelAdmin):
    list_display = ["user", "job_id", "full_name", "reade", "applier", "country", "Descrip", "city_name", "job_title", "Country_of_work", "email", "specifications"]


class CVworkAdmin(admin.ModelAdmin):
    list_display = ["user", "organization", "supervisor_name", "supervisor_telephone_number", "job_title", "supervisor_address", "Duties_and_responsibilities", "start_date", "current_job", "end_date"]


class CVtrainingAdmin(admin.ModelAdmin):
    list_display = ["user", "training_name", "Institution", "Attact_your_certificate", "description_training", "starting_date_teraining", "end_date_teraining"]


class CVrefreeAdmin(admin.ModelAdmin):
    list_display = ["user", "referee_name", "organisation_of_a_referee", "title", "referee_email", "referee_address", "other_attachment1", "CV", "birth_certificate", "recomendation_letter", "TCU_certificate", "other_certificates1", "other_certificates2", "other_certificates3", "other_certificates4"]


admin.site.register(Jobs, JobsAdmin)
admin.site.register(Marked, MarkAdmin)
admin.site.register(CVpersonal, CVpersonalAdmin)
admin.site.register(CVcontact, CVcontactAdmin)
admin.site.register(CVcomputer, CVcomputerAdmin)
admin.site.register(CVaccademic, CVaccademicAdmin)
admin.site.register(CVprofession, CVprofessionAdmin)
admin.site.register(CVlanguage, CVlanguageAdmin)
admin.site.register(CVwork, CVworkAdmin)
admin.site.register(CVtraining, CVtrainingAdmin)
admin.site.register(CVrefree, CVrefreeAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(AcceptedApp, AcceptedAppAdmin)






#
# class MarkAdmin(admin.ModelAdmin):
#     list_display = ["user", "full_name", "location_address", "job_id", "position_type", "job_title", "city_name", "country", "organization", "application_deadline",
#                     "employer_title", "phone_number", "email"]
#


#
# class CVAdmin(admin.ModelAdmin):
#     list_display = ["first_name", "middle_name", "last_name", "Gender", "place_of_birth", "date_of_birth", "Marital_status", "criminal_record", "years_of_work_experience",
#                     "nationality", "disability"]
#
#
#
#
# #
# # admin.site.register(Marked, MarkAdmin)
# # admin.site.register(CV, CVAdmin)
#














