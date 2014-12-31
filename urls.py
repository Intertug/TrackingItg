from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#Agregar ,getRmeolcador
from Mapa.views import getPeru, getMapa, getBoreas, getEosii, getAlisios, getCapidahl, getMistral, getSaga, getTitania, getChinook, getSirocco, getAquavit, getCarex, getVali, getTanok, getSeatrout, getKin, getBarupacifico, getBaruInti #, getCristina, getOdin, getRan

urlpatterns = patterns('',

    #agregar (r'^remolcador$', getRemolcador),
	(r'^$', getMapa),
    (r'^boreas$', getBoreas),
    (r'^eosii$', getEosii),
    (r'^alisios$', getAlisios),
    (r'^capidahl$', getCapidahl),
    (r'^mistral$', getMistral),
    #(r'^cristina$', getCristina),
    (r'^tanok$', getTanok),
    (r'^seatrout$', getSeatrout),
    (r'^kin$', getKin),
    (r'^saga$', getSaga),
    (r'^titania$', getTitania),
    #(r'^odin$', getOdin),
    (r'^vali$', getVali),
    (r'^carex$', getCarex),
    (r'^aquavit$', getAquavit),
    (r'^chinook$', getChinook),
    #(r'^ran$', getRan),
    (r'^sirocco$', getSirocco),
    (r'^barupacifico$', getBarupacifico),
    (r'^baruinti$', getBaruInti),
    (r'^peru$', getPeru),
    
    # Examples:
    # url(r'^$', 'Tracking.views.home', name='home'),
    # url(r'^Tracking/', include('Tracking.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
