from django.conf.urls import patterns, include, url
from django.contrib import admin
from Mapa.views import getBaru, getRan, getTitania, getOceanos, getFrey, getDonLucho, getKronos, getMara, getApolo, getOdin, getColombia, getMexico, getPeru, getBoreas, getEosii, getAlisios, getCapidahl, getMistral, getSaga, getChinook, getSirocco, getCarex, getVali, getTanok, getSeatrout, getKin, getBarupacifico, getBaruInti , getCristina

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'TrackingItg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^boreas$', getBoreas),
    (r'^ran$', getRan),
    (r'^baru$', getBaru),
    (r'^odin$', getOdin),
    (r'^frey$', getFrey),
    (r'^colombia$', getColombia),
    (r'^mexico$', getMexico),
    (r'^eosii$', getEosii),
    (r'^alisios$', getAlisios),
    (r'^donlucho$', getDonLucho),
    (r'^capidahl$', getCapidahl),
    (r'^mistral$', getMistral),
    (r'^cristina$', getCristina),
    (r'^tanok$', getTanok),
    (r'^seatrout$', getSeatrout),
    (r'^kin$', getKin),
    (r'^saga$', getSaga),
    (r'^apolo$', getApolo),
    (r'^mara$', getMara),
    (r'^titania$', getTitania),
    (r'^vali$', getVali),
    (r'^carex$', getCarex),
    (r'^chinook$', getChinook),
    (r'^kronos$', getKronos),
    (r'^sirocco$', getSirocco),
    (r'^oceanos$', getOceanos),
    (r'^barupacifico$', getBarupacifico),
    (r'^baruinti$', getBaruInti),
    (r'^peru$', getPeru),


    url(r'^admin/', include(admin.site.urls)),
)
