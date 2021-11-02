from django.shortcuts import render
from myapp.models import Contact, Custom, Register
from django.contrib import messages

def index(request):
    # return HttpResponse("This is Homepage")
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        messageBox = request.POST.get('messageBox')
        contact = Contact(name=name, email=email, phone=phone, messageBox=messageBox)
        contact.save()
        messages.success(request, f'Hello {name}! Thank you contacting us. We will get back to you soon.')
    return render(request, 'contact.html')
    # return HttpResponse("This is contact page")

def custom(request):
    if request.method == 'POST':
        customFlowerName = request.POST.get('customFlowerName')
        customSizeOfBouquet = request.POST.get('customSizeOfBouquet')
        customBouquetPicture = request.POST.get('customBouquetPicture')
        custom = Custom(customFlowerName=customFlowerName, customSizeOfBouquet=customSizeOfBouquet, customBouquetPicture=customBouquetPicture )
        custom.save()
        messages.success(request, 'Thank you for your order. We will send you the order details')
    return render(request, 'custom.html')

def register(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('username')
        password = request.POST.get('password')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        register = Register(firstName=firstName, lastName=lastName, username=username, password=password, city=city, state=state, zipcode=zipcode )
        register.save()
        messages.success(request, f'{firstName}, you have been registered successfully')
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

