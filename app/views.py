from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from app.models import contact,donation






def contacts(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        message1 = request.POST.get('message')

        Contact = contact(name = name1,email =email1, phone =phone1, message=message1)
        Contact.save()
        print("user created") 
        return redirect('/')

    else:
        return render(request , "contacts.html")
    



     
def home(request):
    return render(request , "index.html")

def gallery(request):
    return render(request , "gallery.html")

def team(request):
    return render(request , "ourteam.html")

           
def donate(request):
    if request.method == 'POST':
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        phone1 = request.POST.get('phone')
        pancard1 = request.POST.get('pan')
        amount1 = request.POST.get('amount')
        address1 = request.POST.get('address')

        donate = donation(name = name1,email =email1, phone =phone1, pancard = pancard1, amount = amount1, address = address1)
        donate.save()
        print("user created") 
        return redirect('/')

    else:
        return render(request , "donation.html")
    
