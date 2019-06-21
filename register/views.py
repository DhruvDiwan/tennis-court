from django.shortcuts import render
from register.models import Person , MobNo , Username , Password
from django.http import HttpResponse

def homePageView(request):
    return render(request ,'home.html')

def profilePageView(request):
    return render(render , 'profile.html')

def addUser(request):
    user_ = Person.objects.create(fName = request.POST['fName'] , sName = request.POST['sName'])
    MobNo.objects.create(phone_number = request.POST['mobNo'] , person = user_)
    Username.objects.create(username = request.POST['username'] , person = user_)
    Password.objects.create(password = request.POST['Confirm pass'] , person = user_)
    return HttpResponse("User added")
