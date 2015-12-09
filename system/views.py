from models import Student,Teacher,User,Usert
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

def home_t(request):
    return render_to_response("home-t.html")


def search(request):
    if request.GET:
        tea=Teacher.objects.get(Username=request.GET["myt"])
        c = Context({"tea":tea,})
        return render_to_response("search2.html",c)
    else:
        return render_to_response("search.html")

def request_(request):    

    teacherlist = Teacher.objects.all()   
    c = Context({"teacherlist":teacherlist})
##    else:
##        return HttpResponse("Not right password!")
#        #return render_to_response("request.html",c) 
    return render_to_response("request.html",c)
'''
    if request and "requestdate" in request.GET:
        #print request.GET["requestdate"]
        #request_date = request.GET["requestdate"]
        #rt = request.GET["requestteacher"]
        u=User.objects.all()
        for mu in u:
            mu1=mu
        
        Student.objects.get(Username = mu1.Username).update(
        
        Myrequestdate = GET["requestdate"],
        Myrequestteacher = post["requestteacher"],
          
    return render_to_response("request.html",c)
''' 
def requestt(request):
    u=Usert.objects.all()
    for mu in u:
        mu1=mu
    stu=Student.objects.filter(Myrequestteacher=mu1.Username)
    c = Context({"stu":stu,})
    return render_to_response("request-t.html",c) 
    
def recommand(request):
    if request.GET:
        tea=Teacher.objects.get(Research_area=request.GET["area"])
        c = Context({"tea":tea,})
        return render_to_response("recommand2.html",c)
    else:
        
        return render_to_response("recommand.html")
    
def new(request):
    teachers = Teacher.objects.all()

    return render_to_response("news.html",{'teachers':teachers})

def newt(request):
    if request.POST:
        post = request.POST
        u=Usert.objects.all()
        for mu in u:
            mu1=mu
        myu = Teacher.objects.get(Username = mu1.Username)
        myu.Information = post["news"]
        myu.save()
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

def logint(request):
    if request.GET:
        teau=Teacher.objects.get(Username = request.GET["username"])
        c = Context({"teau":teau,})
        if request.GET["password"] == teau.Password:
            Usert.objects.create(Username= teau.Username,Password=teau.Password)
            return render_to_response("home-t.html",c)
        else:
            return HttpResponse("Not right password!")
    else:
        return render_to_response("login-t.html")
    
def informationt(request):
    u=Usert.objects.all()
    for mu in u:
        mu1=mu
    myu = Teacher.objects.get(Username = mu1.Username)
    c=Context({"myu":myu,})
    if request.POST:
        post = request.POST
        if post["research_area"] and post["introduction"] and post["email"]:
            
            myu.Research_area = post["research_area"]     
            myu.Introduction = post["introduction"]
            #myu. = post[""]
            myu.Email = post["email"]   
            myu.save()
        else:
            return HttpResponse('Please full all information.')
    return render_to_response("information-t.html",c)
    
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



def information(request):
    u=User.objects.all()
    for mu in u:
        mu1=mu
    myu = Student.objects.get(Username = mu1.Username)
    c=Context({"myu":myu,})
    if request.POST:
        post = request.POST
        if post["number"] and post["institute"] and post["contact_way"] and post["email"]:
            
            myu.Number = post["number"]     
            myu.Institute = post["institute"]
            myu.Contact_way = post["contact_way"]
            myu.Email = post["email"]   
            myu.save()
        else:
            return HttpResponse('Please full all information.')
    return render_to_response("information.html",c)
    
    
