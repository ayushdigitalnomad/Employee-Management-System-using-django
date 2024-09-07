from django.shortcuts import render,HttpResponse,redirect
from .models import company,employee,Testimonial
from django.utils import timezone
from .forms import FeedbackForm,employeeform
from auth_app.middleware import auth
"""employeeform"""

# Create your views here.
@auth
def Company(request):
    emps=employee.objects.all()
    return render(request,"home.html",{"emps":emps})
def add_emp(request):
    #data fetch
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_designation=request.POST.get("emp_designation")
        # create model object and set the data
        e=employee()
        e.name=emp_name
        e.employee_id=emp_id
        e.phone_no=emp_phone
        e.address=emp_address
        if emp_working is None:
            e.Working=False
        else:
            e.Working=True
        e.designation=emp_designation
        # save the object
        e.save()
        # prepare the msg
        return redirect("/home/")
    #form=employeeform()
    #form.save()
  #  return render(request,"add.html",{'form':form})
    return render(request,"add.html",{})

def delete_emp(request,employee_id):
    print(employee_id)
    emp=employee.objects.get(pk=employee_id)
    emp.delete()
    return redirect("/home/")
def update_emp(request,employee_id):
    emp = employee.objects.get(pk=employee_id)
    return render(request,"update.html",{"emp": emp })
def do_update(request,employee_id):
    emp = employee.objects.get(pk=employee_id)
    if request.method == "POST":
        emp_name = request.POST.get("emp_name")
        employee_id_temp = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working")
        emp_designation = request.POST.get("emp_designation")
        print(employee_id)
        e = employee.objects.get(pk=employee_id)
        e.name = emp_name
        e.employee_id = employee_id_temp
        e.phone_no = emp_phone
        e.address = emp_address
        if emp_working is None:
            e.Working = False
        else:
            e.Working = True
        e.designation = emp_designation
        e.save()
        return redirect("/home/")
    return render(request, "update.html", {"emp": emp})



def Testimonials(request):
    testi=Testimonial.objects.all()
    return render(request,"testimonials.html",{"testi":testi})
def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            """print(form.cleaned_data['email_id'])
            print(form.cleaned_data['name'])
            print(form.cleaned_data['feedback'])
            print("data saved")"""
            form.save()
        else:
            return render(request, 'feedbackform.html', {"form": form})
    else:
        form = FeedbackForm()
        return render(request,'feedbackform.html',{"form":form})








