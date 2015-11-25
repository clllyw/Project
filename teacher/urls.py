from django.conf.urls import patterns,url

from django.conf import settings
from django.conf.urls.static import static
from system.views import home, search, request_, requestt, recommand, new, registert, login, informationt, register,home_t,information

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teacher.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
    url(r'^$', 'system.views.home'),
    url(r'^search/$', 'system.views.search'),
    url(r'^request/$', 'system.views.request_'),
    url(r'^requestt/$', 'system.views.requestt'),
    url(r'^recommand/$', 'system.views.recommand'),
    url(r'^new/$', 'system.views.new'),
    url(r'^newt/$', 'system.views.newt'),
    url(r'^registert/$', 'system.views.registert'),
    url(r'^login/$', 'system.views.login'),
    url(r'^informationt/$', 'system.views.informationt'),
     url(r'^t/$', 'system.views.home_t'),
    url(r'^register/$', 'system.views.register'),
    url(r'^infor/$', 'system.views.information'),

    url(r'^staticfiles/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),
    #url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )
