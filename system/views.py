from models import Student,Teacher,User,Usert,New,Appointment
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

arealist = set()

    

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
def deleteapp(request):
    ta=Appointment.objects.get(id=request.GET["id"])
    ta.delete()
    u=User.objects.all()
    for mu in u:
        mu1=mu
    applist=Appointment.objects.filter(stu_name=mu1.Username)
    c = Context({"applist":applist,})
    return render_to_response("requestm.html",c)

def requestm(request):    
    u=User.objects.all()
    for mu in u:
        mu1=mu
    applist=Appointment.objects.filter(stu_name=mu1.Username)
    c = Context({"applist":applist,})
    return render_to_response("requestm.html",c)
#    teacherlist = Teacher.objects.all()   
#    c = Context({"teacherlist":teacherlist})
##    else:
##        return HttpResponse("Not right password!")
#        #return render_to_response("request.html",c) 
#    return render_to_response("request.html",c)
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
def addapp(request):
    fff = True
    teacherlist = Teacher.objects.all()   
    c = Context({"teacherlist":teacherlist})
    u=User.objects.all()
    for mu in u:
        mu1=mu
    if "seleted_teacher" in request.POST:
        tea=Teacher.objects.get(id=request.POST["seleted_teacher"])
        apps = Appointment.objects.filter(tea_name = tea.Username)
        for t in apps:
            if t.app_time == request.POST["requestdate"]:
                fff = False
        if fff == True:
            new_appointment = Appointment( 
            stu_name =  mu1.Username,
            tea_name = tea.Username,
            app_time = request.POST["requestdate"],
            flag = "no")       
            new_appointment.save()
            u=User.objects.all()
            for mu in u:
                mu1=mu
            applist=Appointment.objects.filter(stu_name=mu1.Username)
            c = Context({"applist":applist,})
            return render_to_response("requestm.html",c)
        else:
            return HttpResponse("Time interrupt!")
    
    else:
        return render_to_response("request.html",c)
   
      
def updateapp(request):
    fff = True
    app = Appointment.objects.get(id=request.GET["id"])
    if request.POST:
        apps = Appointment.objects.filter(tea_name = app.tea_name)
        for t in apps:
            if t.app_time == request.POST["requestdate"]:
                fff = False
        if fff == True:
            Appointment.objects.filter(id=request.GET["id"]).update(
            app_time = request.POST["requestdate"])
            u=User.objects.all()
            for mu in u:
                mu1=mu
            applist=Appointment.objects.filter(stu_name=mu1.Username)
            c = Context({"applist":applist,})
            return render_to_response("requestm.html",c)
        else:
            return HttpResponse("Time interrupt!")
    else:
        return render_to_response("request2.html") 
def requestt(request):
    u=Usert.objects.all()
    for mu in u:
        mu1=mu
    ap=Appointment.objects.filter(tea_name=mu1.Username)
    ap1=ap.filter(flag="no")
    ap2=ap.filter(flag="yes")
    c = Context({"ap":ap,"ap1":ap1,"ap2":ap2})
    return render_to_response("request-t.html",c) 

def confirm(request):
    a=Appointment.objects.get(id=request.GET["id"])
    a.flag="yes"
    a.save()
    u=Usert.objects.all()
    for mu in u:
        mu1=mu
    ap=Appointment.objects.filter(tea_name=mu1.Username)
    ap1=ap.filter(flag="no")
    ap2=ap.filter(flag="yes")
    c = Context({"ap":ap,"ap1":ap1,"ap2":ap2})
    return render_to_response("request-t.html",c) 
    
def recommand(request):
    if request.GET:
        areal=[]
        for ar in arealist:
            areal.append(ar)
        tea=Teacher.objects.filter(Research_area=areal[int(request.GET["area"])])
        c = Context({"tea":tea,})
        return render_to_response("recommand2.html",c)
    else:
        teacherlist = Teacher.objects.all()
#        arealist = set()
        for t in teacherlist:
            arealist.add(t.Research_area)
        #c = Context({"teacherlist":teacherlist})
        c = Context({"arealist":arealist})
        return render_to_response("recommand.html",c)
    
def new(request):
    mynew = New.objects.all()
    return render_to_response("news.html",{'mynew':mynew})

def newt(request):

    u=Usert.objects.all()
    for mu in u:
        mu1=mu

    newslist=New.objects.filter(er=mu1.Username)      

    return render_to_response("news-tm.html",{'newslist':newslist})
    
def addnew(request):
    if request.POST:
        post = request.POST
        u=Usert.objects.all()
        for mu in u:
            mu1=mu

        new_New = New(
        er = mu1.Username,
        Information= post["news"]) 
        new_New.save()        
    return render_to_response("news-t.html")
def updatenew(request):
    tn=New.objects.get(id=request.GET["id"])
    bc = Context({"tn":tn,})
    if request.POST:
        post = request.POST
        if post["news"]:
            
            tn.Information= post["news"]     
            tn.save()

    return render_to_response("news-tu.html",bc)
def deletenew(request):
    tn=New.objects.get(id=request.GET["id"])
    tn.delete()
    u=Usert.objects.all()
    for mu in u:
        mu1=mu
    newslist=New.objects.filter(er=mu1.Username)  
    return render_to_response("news-tm.html", {'newslist':newslist})
    
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
    
    
