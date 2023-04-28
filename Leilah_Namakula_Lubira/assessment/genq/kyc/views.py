from django.shortcuts import render
from django.contrib import messages 
from .models import Registration

# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request): 
    if request.POST =='POST':
        fname= request.POST['firstname']
        lname = request.POST['lastname']
        Dob = request.POST['Date_of_birth']
        gen = request.POST['gender']
        cou = request.POST['country']
        sta = request.POST['state']
        towns = request.POST['town']
        zipcodes = request.POST['zipcode']
        phone1s = request.POST['phone1']
        phone2s = request.POST['phone2']
        emails = request.POST['email']

        details = Registration(
            firstname = fname,
            lastname = lname,
            Date_of_birth = Dob,
            gender = gen,
            country = cou,
            state = sta,
            town = towns,
            zipcode = zipcodes,
            phone1 = phone1s,
            phone2 = phone2s,
            email = emails
        )
        details.save()
        chats = Registration.objects.all()
        messages.success(request, ("Form has been submitted successfully!"))  
            

        return render(request, 'index.html')#{'messages':messages})
    else:
        return render(request,'index.html')
    

