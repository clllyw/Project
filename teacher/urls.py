from django.conf.urls import patterns,url

from django.conf import settings
from django.conf.urls.static import static
from system.views import home, search, requestm,addapp,deleteapp,updateapp, requestt, recommand, new, registert, login, informationt, register,home_t,information,logint,deletenew,addnew,updatenew

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teacher.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
    url(r'^$', 'system.views.home'),
    url(r'^search/$', 'system.views.search'),
    url(r'^request/$', 'system.views.requestm'),
    url(r'^requestt/$', 'system.views.requestt'),
    url(r'^recommand/$', 'system.views.recommand'),
    url(r'^new/$', 'system.views.new'),
    url(r'^newt/$', 'system.views.newt'),
    url(r'^registert/$', 'system.views.registert'),
    url(r'^login/$', 'system.views.login'),
    url(r'^logint/$', 'system.views.logint'),                       
    url(r'^informationt/$', 'system.views.informationt'),
    url(r'^t/$', 'system.views.home_t'),
    url(r'^register/$', 'system.views.register'),
    url(r'^infor/$', 'system.views.information'),
    url(r'^deletenew/$', 'system.views.deletenew'),
    url(r'^addnew/$', 'system.views.addnew'),
    url(r'^updatenew/$', 'system.views.updatenew'),
    url(r'^addapp/$', 'system.views.addapp'),
    url(r'^apptime/$', 'system.views.apptime'),
    url(r'^deleteapp/$', 'system.views.deleteapp'),
    url(r'^updateapp/$', 'system.views.updateapp'),
    url(r'^confirm/$', 'system.views.confirm'),
    url(r'^staticfiles/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),
    #url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
