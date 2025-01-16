from django.contrib import admin
from HospitalApp.models import*
# Register your models here.


admin.site.site_header = 'Hospital | Manoj Gain' 

class AdminDoctor(admin.ModelAdmin):
    list_display = ['id','name','mobile','special','created_at','updated_at']
admin.site.register(Doctor, AdminDoctor)


class AdminPatient(admin.ModelAdmin):
    list_display = ['id','name','mobile','gender','created_at','updated_at']
admin.site.register(Patient, AdminPatient)


class AdminAppointment(admin.ModelAdmin):
    list_display = ['id','doctor','patient','date1','time1','created_at','updated_at']
admin.site.register(Appointment, AdminAppointment)