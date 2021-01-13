from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request): # *args, **kwargs
	#print(args,kwargs)
	print(request.user)
	return render(request, "home.html",{}) # string of HTML code


def contact_view(request): # *args, **kwargs
	#print(args,kwargs)
	print(request.user)
	my_context = {
		"my_text": "this is about me",
		"my_number": 123,
		"my_list":[1,2,3],
	}
	return render(request, "contact.html",my_context) # string of HTML code


def about_view(request): # *args, **kwargs
	#print(args,kwargs)
	print(request.user)
	return HttpResponse('<h1>About Page</h1>') # string of HTML code


def social_view(request): # *args, **kwargs
	#print(args,kwargs)
	print(request.user)
	return HttpResponse('<h1>Social Page</h1>') # string of HTML code