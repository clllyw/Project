
from django.shortcuts import render_to_response
# Create your views here.
def home(request):
    return render_to_response("home.html")
    
def search(request):
    return render_to_response("search.html")

def request(request):
    return render_to_response("request.html")    
    
def requestt(request):
    return render_to_response("request-t.html") 
    
def recommand(request):
    return render_to_response("recommand.html")
    
def new(request):
    return render_to_response("new.html")

def newt(request):
    return render_to_response("new-t.html")

def registert(request):
    return render_to_response("register-t.html")    
    
def login(request):
    return render_to_response("login.html")

def informationt(request):
    return render_to_response("information-t.html")
    
def register(request):
    return render_to_response("gegister.html")

def home_t(request):
    return render_to_response("home-t.html")

def information(request):
    return render_to_response("information.html")
    
    
