from django.shortcuts import render,redirect
from .models import Person
# Create your views here.



def home(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        person = Person.objects.create(username=uname, email=email, phone=phone)
        person.save()
        return redirect('/')
    personobj = Person.objects.all().order_by('-id')
    return render(request, 'index.html',context={'person':personobj})