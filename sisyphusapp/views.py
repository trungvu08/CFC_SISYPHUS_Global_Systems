from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib import messages
from sisyphusapp.models import Contact 

# Create your views here.
def index(request):
	return render(request, "index.html")

def green_grey(request):
	return render(request, "green_grey.html")

def ar_map_demo(request):
	return render(request, "ar_map_demo.html")

def ar_home_demo(request):
	return render(request, "ar_home_demo.html")

def helpcenter(request):
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		desc = request.POST.get('desc')
		contact = Contact(name=name, email=email, desc=desc, date=datetime.today()) 
		contact.save()
		messages.success(request, 'Your message has been sent!')

	return render(request, 'contact.html')  
	

