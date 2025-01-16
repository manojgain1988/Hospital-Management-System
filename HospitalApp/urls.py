from django.urls import path
from HospitalApp import views

urlpatterns = [
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   
   path('add-doctor/', views.add_doctor, name='add-doctor'),
   path('view-doctor/', views.view_doctor, name='view-doctor'),
   path('delete-doctor(<int:pid>)', views.delete_doctor, name='delete-doctor'),
   
   path('add-patient/', views.add_patient, name='add-patient'),
   path('view-patient/', views.view_patient, name='view-patient'),
   
   path('add-appointment/', views.add_appointment, name='add-appointment'),
   path('view-appointment/', views.view_appointment, name='view-appointment'),
   
   path('admin_login/', views.Login, name='login'),
   path('logout/', views.Logout_admin , name='logout'),
   
]
 