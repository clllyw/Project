from models import Student,Teacher,User
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
#def custom_proc(request):
#    "A context processor that provides 'user'."
#    return {
#    
#        'user': request.user,
#        'ip_address': request.META['REMOTE_ADDR']
#    }

def home(request):
    return render_to_response("home.html")
    
def search(request):
    return render_to_response("search.html")

def request_(request):    
#    if "requestdate" in request.GET:
#        #print request.GET["requestdate"]
#        request_date = request.GET["requestdate"]
#        c = Context({"request_date":request_date,})
##    else:
##        return HttpResponse("Not right password!")
#        #return render_to_response("request.html",c) 
#        return render_to_response("new.html")
    if request:
        
        teacherlist = Teacher.objects.all()   
        c = Context({"teacherlist":teacherlist})
        return render_to_response("request.html",c)
    
def requestt(request):
    return render_to_response("request-t.html") 
    
def recommand(request):
    return render_to_response("recommand.html")
    
def new(request):
    return render_to_response("news.html")

def newt(request):
    return render_to_response("new-t.html")

def registert(request):
    if request.POST:
        post = request.POST
        new_teacher = Teacher(
        Username = post["username"],
        Password= post["password"],
        Research_area = post["research_area"],
        Email = post["email"],
        Introduction  = post["introduction"]) 
        new_teacher.save()
    return render_to_response("register-t.html")    
    
def login(request):
    if request.GET:
        stu=Student.objects.get(Username = request.GET["username"])
        c = Context({"stu":stu,})
        if request.GET["password"] == stu.Password:
            User.objects.create(Username= stu.Username,Password=stu.Password)
            return render_to_response("home.html",c)
        else:
            return HttpResponse("Not right password!")
    else:
        return render_to_response("login.html")

def informationt(request):
    return render_to_response("information-t.html")
    
def register(request):
    if request.POST:
        post = request.POST
        new_student = Student(
        Username = post["username"],
        Password= post["password"],
        Institute = post["institute"],
        Contact_way  = post["contact_way"],
        Email = post["email"]) 
        new_student.save()
    return render_to_response("gegister.html")

def home_t(request):
    return render_to_response("home-t.html")

def information(request):
    u=User.objects.all()
    for mu in u:
        c=Context({"mu":mu,}) 
    return render_to_response("information.html",c)
    
    
