from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from HospitalApp.models import*

# Create your views here.

def about(request):
    context={}
    return render(request,'about.html',context)


def index(request):
    if not request.user.is_staff:
        return redirect('login')
    context={}
    return render(request,'index.html',context)



def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pword']
        
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user) 
                error = 'no'              
            else:
                error='yes'
        except:
            error='yes'            
    context={
        'error': error,
    }
    return render(request,'login.html',context)



def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')



def contact(request):
    context={}
    return render(request,'contact.html',context)



def add_doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
    
        try:
            Doctor.objects.create(name=n, mobile=c, special=sp) 
            error = 'no'              
        except:
            error='yes'            
    context={
        'error': error,
    }
    return render(request,'add_doctor.html',context)


def view_doctor(request):
    doctors = Doctor.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    context={
        'doctors': doctors
    }
    return render(request,'view_doctor.html',context)



def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doctor.objects.get(id=pid)
    doctors.delete()
    return redirect('view-doctor')




def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    context={
        "pat":pat,
    }
    return render(request,'view_patient.html',context)




def add_patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['mobile']
        a = request.POST['address']
    
        try:
            Patient.objects.create(name=n, gender=g, mobile=m, address=a) 
            error = 'no'              
        except:
            error='yes'            
    context={
        'error': error,
    }
    return render(request,'add_patient.html',context)




def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view-patient')



def add_appointment(request):
    context={}
    return render(request,'add_appointment.html',context)


def view_appointment(request):
    context={}
    return render(request,'view_appointment.html',context)






