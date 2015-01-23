# Create your views here.
from django.shortcuts import render_to_response
from Mapa.models import *
from django.db import connection

def getPropulsor(request, nom, lado):

	cursorPropB = connection.cursor()

	if 'fecha' in request.GET:
		fecha = request.GET['fecha']
		hora1 = request.GET['hora1']
		hora2 = request.GET['hora2']
		minutos1 = request.GET['minutos1']
		minutos2 = request.GET['minutos2']
		cursorPropB.execute("select fechahora, totalhours, totalfuel, enginespeed, percentload, fuelrate, coolanttemperature, oiltemperature, oilpressure, intercoolertemperature from propulsor where (fechahora between '" + str(fecha) + " " + str(hora1) + ":" + str(minutos1) + "' and '" + str(fecha) + " " + str(hora2) + ":" + str(minutos2) + "') and rm ='" + str(nom) + "' and side='"+ str(lado) +"' order by fechahora desc limit 1;")			
	else:
		cursorPropB.execute("select fechahora, totalhours, totalfuel, enginespeed, percentload, fuelrate, coolanttemperature, oiltemperature, oilpressure, intercoolertemperature from propulsor where rm = '"+ str(nom) +"' and side='"+ str(lado) +"' order by fechahora desc limit 1;")
	#cursorPropB.execute("select fechahora, totalhours, totalfuel, enginespeed, percentload, fuelrate, coolanttemperature, oiltemperature, oilpressure, intercoolertemperature from propulsor where rm = '"+ str(nom) +"' and side='"+ str(lado) +"' and (fechahora > '2014-05-19 02:25:00' and fechahora < '2014-05-19 02:26:00');")
	rowsPropB = cursorPropB.fetchall()

	return rowsPropB

def getGenerador(request, nom, lado):

	cursor = connection.cursor()

	if 'fecha' in request.GET:
		fecha = request.GET['fecha']
		hora1 = request.GET['hora1']
		hora2 = request.GET['hora2']
		minutos1 = request.GET['minutos1']
		minutos2 = request.GET['minutos2']
		cursor.execute("select fechahora, totalhours, triphours, startcounter, rpmmeter, ch1, ch2, ch3, ch4, ch5, batteryvoltage from generador where (fechahora between '" + str(fecha) + " " + str(hora1) + ":" + str(minutos1) + "' and '" + str(fecha) + " " + str(hora2) + ":" + str(minutos2) + "') and rm ='" + str(nom) + "' and side='"+ str(lado) +"' order by fechahora desc limit 1;")
	else:
		cursor.execute("select fechahora, totalhours, triphours, startcounter, rpmmeter, ch1, ch2, ch3, ch4, ch5, batteryvoltage from generador where rm = '"+ str(nom) +"' and side='"+ str(lado) +"' order by fechahora desc limit 1;")
	#cursor.execute("select fechahora, totalhours, triphours, startcounter, rpmmeter, ch1, ch2, ch3, ch4, ch5, batteryvoltage from generador where rm = '"+ str(nom) +"' and side='portside' and (fechahora > '2014-05-19 02:25:00' and fechahora < '2014-05-19 02:26:00');")
	
	rows = cursor.fetchall()

	return rows

def llenarMatriz(rows):

	matriz = []
	norte = []
	sur = []
	for i in range(len(rows)):
		norte.append(rows[i][0])
		sur.append(rows[i][2])
		norteHoras = norte[i] // 100
		norteMinutos = norte[i] % 100
		if rows[i][1] == 'S':
			coordenadaNorte = -(norteHoras + norteMinutos / 60)
		else:
			coordenadaNorte = norteHoras + norteMinutos / 60
		surHoras = sur[i] // 100
		surMinutos = sur[i] % 100
		if rows[i][3] == 'W':
			coordenadaSur = -(surHoras + surMinutos / 60)
		else:
			coordenadaSur = surHoras + surMinutos / 60
		
		matriz.append({
			'rm': rows[i][6], 
			'latitud': coordenadaNorte,
			'longitud': coordenadaSur,
			'velocidad': rows[i][4],
			'fechahora': rows[i][5],
			})

	return matriz

def getGps(request, rem):

	cursorGps = connection.cursor()

	if 'fecha' in request.GET:
		fecha = request.GET['fecha']
		hora1 = request.GET['hora1']
		hora2 = request.GET['hora2']
		minutos1 = request.GET['minutos1']
		minutos2 = request.GET['minutos2']
		cursorGps.execute("select latitud, latitudNS, longitud, longitudEW, velocidad, fechahora, rm from gps where (fechahora between '" + str(fecha) + " " + str(hora1) + ":" + str(minutos1) + "' and '" + str(fecha) + " " + str(hora2) + ":" + str(minutos2) + "') and rm ='" + str(rem) + "';")			
	else:
		cursorGps.execute("select latitud, latitudNS, longitud, longitudEW, velocidad, fechahora, rm from gps where (fechahora between (NOW() - CURTIME()) AND NOW()) and rm ='"+ str(rem) +"';")
	
	rowsG = cursorGps.fetchall()
	matrizGps = llenarMatriz(rowsG)
	
	#if not matrizGps:
	#	cursorGps.execute("select latitud, latitudNS, longitud, longitudEW, velocidad, fechahora, rm from gps where rm ='"+ str(rem) +"' order by fechahora desc limit 1440;")
	#	rowsG = cursorGps.fetchall()
	#	matrizGps = llenarMatriz(rowsG)
	
	return matrizGps

def llenarMapa(nombre):

	cursorAlisios = connection.cursor()
	#cursorAlisios.execute("select latitud, latitudNS, longitud, longitudEW, velocidad, fechahora, rm from gps where rm = '"+str(nombre)+"' order by id desc limit 1;")
	cursorAlisios.execute("select top 1 Latitude, LatitudeNS, Longitude, LongitudeEW, Speed, TimeString from [2150-DAQOnBoardGps] where vesselname = '"+str(nombre)+"' order by TimeString desc;")
	rowsA = cursorAlisios.fetchall()
	matrizA =  llenarMatriz(rowsA)
	loopAlisios = [matrizA[0]['latitud'], matrizA[0]['longitud'], matrizA[0]['velocidad'], matrizA[0]['fechahora']]

	return loopAlisios

def getMapa(request):
	
	#agregar loopRemolcador = llenarMapa('remolcador')
	loopBoreas = llenarMapa('boreas')
	loopAlisios = llenarMapa('alisios')
	loopEosii = llenarMapa('eosii')
	loopCapidahl = llenarMapa('capidahl')
	loopMistral = llenarMapa('mistral')
	loopSaga = llenarMapa('saga')
	loopTitania = llenarMapa('titania')
#	loopCristina = llenarMapa('cristina')
	loopTanok = llenarMapa('tanok')
	loopSeatrout = llenarMapa('seatrout')
	loopKin = llenarMapa('kin')
	loopChinook = llenarMapa('chinook')
#	loopOdin = llenarMapa('odin')
	loopVali = llenarMapa('vali')
	loopCarex = llenarMapa('carex')
	loopAquavit = llenarMapa('aquavit')
#	loopRan = llenarMapa('ran')
	loopSirocco = llenarMapa('sirocco')
	loopBarupacifico = llenarMapa('barupacifico')
	loopBaruInti = llenarMapa('baruinti')

	return render_to_response('mapa.html', locals())

def getPeru(request):
	
	#agregar loopRemolcador = llenarMapa('remolcador')
	loopMistral = llenarMapa('MISTRAL')
	loopVali = llenarMapa('VALI')
	loopBarupacifico = llenarMapa('BARU PACIFICO')
	loopBaruInti = llenarMapa('BARU INTI')

	return render_to_response('peru.html', locals())

def getCapidahl(request):
	
	gps = getGps(request, 'capidahl')

	rowsPropB = getPropulsor(request, 'capidahl', 'portside')
	rowsPropE = getPropulsor(request, 'capidahl', 'starboard')
	rowsGenB = getGenerador(request,'capidahl', 'portside')
	rowsGenE = getGenerador(request,'capidahl', 'starboard')
	
	matrizGps = gps

	loopCapidahl = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'capidahl':
			loopCapidahl.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('capidahl.html', locals())

# agregar a cada remolcador:
# def getRemolcador(request):
	
# 	gps = getGps(request, 'remolcador')

# 	#agregar si se tiene daq en propulsor y generador
#  	#rowsPropB = getPropulsor(request, 'remolcador', 'portside') 
#  	#rowsPropE = getPropulsor(request, 'remolcador', 'starboard') 
#  	#rowsGenB = getGenerador(request,'remolcador', 'portside')
#  	#rowsGenE = getGenerador(request,'remolcador', 'starboard')
	
#  	matrizGps = gps

#  	loopRemolcador = []

#  	for i in range(len(matrizGps)):
#  		if matrizGps[i]['rm'] == 'remolcador':
#  			loopRemolcador.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

#  	return render_to_response('remolcador.html', locals())

def getChinook(request):
	
	gps = getGps(request, 'chinook')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopChinook = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'chinook':
			loopChinook.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('chinook.html', locals())

def getBarupacifico(request):
	
	gps = getGps(request, 'barupacifico')

	rowsPropB = getPropulsor(request, 'barupacifico', 'portside')
	rowsPropE = getPropulsor(request, 'barupacifico', 'starboard')
	rowsGenB = getGenerador(request,'barupacifico', 'portside')
	rowsGenE = getGenerador(request,'barupacifico', 'starboard')
	
	matrizGps = gps

	loopBarupacifico = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'barupacifico':
			loopBarupacifico.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('barupacifico.html', locals())

def getBaruInti(request):
	
	gps = getGps(request, 'baruinti')

	#rowsPropB = getPropulsor(request, 'baruinti', 'portside')
	#rowsPropE = getPropulsor(request, 'baruinti', 'starboard')
	#rowsGenB = getGenerador(request,'baruinti', 'portside')
	#rowsGenE = getGenerador(request,'baruinti', 'starboard')
	
	matrizGps = gps

	loopBaruInti = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'baruinti':
			loopBaruInti.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('baruinti.html', locals())

# def getOdin(request):
	
# 	gps = getGps(request, 'odin')

# 	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
# 	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
# 	#rowsGenB = getGenerador(request,'mistral', 'portside')
# 	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
# 	matrizGps = gps

# 	loopOdin = []

# 	for i in range(len(matrizGps)):
# 		if matrizGps[i]['rm'] == 'odin':
# 			loopOdin.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

# 	return render_to_response('odin.html', locals())

def getVali(request):
	
	gps = getGps(request, 'vali')

	rowsPropB = getPropulsor(request, 'vali', 'portside')
	rowsPropE = getPropulsor(request, 'vali', 'starboard')
	rowsGenB = getGenerador(request,'vali', 'portside')
	rowsGenE = getGenerador(request,'vali', 'starboard')
	
	matrizGps = gps

	loopVali = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'vali':
			loopVali.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('vali.html', locals())

def getCarex(request):
	
	gps = getGps(request, 'carex')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopCarex = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'carex':
			loopCarex.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('carex.html', locals())

def getAquavit(request):
	
	gps = getGps(request, 'aquavit')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopAquavit = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'aquavit':
			loopAquavit.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('aquavit.html', locals())

# def getRan(request):
	
# 	gps = getGps(request, 'ran')

# 	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
# 	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
# 	#rowsGenB = getGenerador(request,'mistral', 'portside')
# 	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
# 	matrizGps = gps

# 	loopRan = []

# 	for i in range(len(matrizGps)):
# 		if matrizGps[i]['rm'] == 'ran':
# 			loopRan.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

# 	return render_to_response('ran.html', locals())

def getSirocco(request):
	
	gps = getGps(request, 'sirocco')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopSirocco = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'sirocco':
			loopSirocco.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('sirocco.html', locals())

# def getCristina(request):
	
# 	gps = getGps(request, 'cristina')

# 	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
# 	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
# 	#rowsGenB = getGenerador(request,'mistral', 'portside')
# 	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
# 	matrizGps = gps

# 	loopCristina = []

# 	for i in range(len(matrizGps)):
# 		if matrizGps[i]['rm'] == 'cristina':
# 			loopCristina.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

# 	return render_to_response('cristina.html', locals())

def getTanok(request):
	
	gps = getGps(request, 'tanok')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopTanok = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'tanok':
			loopTanok.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('tanok.html', locals())

def getSeatrout(request):
	
	gps = getGps(request, 'seatrout')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopSeatrout = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'seatrout':
			loopSeatrout.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('seatrout.html', locals())

def getKin(request):
	
	gps = getGps(request, 'kin')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopKin = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'kin':
			loopKin.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('kin.html', locals())

def getTitania(request):
	
	gps = getGps(request, 'titania')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopTitania = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'titania':
			loopTitania.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('titania.html', locals())
	
def getSaga(request):
	
	gps = getGps(request, 'saga')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopSaga = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'saga':
			loopSaga.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('saga.html', locals())

def getMistral(request):
	
	gps = getGps(request, 'mistral')

	rowsPropB = getPropulsor(request, 'mistral', 'portside')
	rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	rowsGenB = getGenerador(request,'mistral', 'portside')
	rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopMistral = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'mistral':
			loopMistral.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('mistral.html', locals())

def getBoreas(request):

	gps = getGps(request, 'boreas')

	rowsPropB = getPropulsor(request, 'boreas', 'portside')
	rowsPropE = getPropulsor(request, 'boreas', 'starboard')
	#rowsGenB = getGenerador(request,'boreas', 'portside')
	#rowsGenE = getGenerador(request,'boreas', 'starboard')
	
	matriz = gps

	loopBoreas = []

	for i in range(len(matriz)):
		if matriz[i]['rm'] == 'boreas':
			loopBoreas.append([matriz[i]['latitud'], matriz[i]['longitud'], matriz[i]['velocidad'], matriz[i]['fechahora']])

	return render_to_response('boreas.html', locals())


def getEosii(request):
	
	gps = getGps(request, 'eosii')

	rowsPropB = getPropulsor(request, 'eosii', 'portside')
	rowsPropE = getPropulsor(request, 'eosii', 'starboard')
	rowsGenB = getGenerador(request,'eosii', 'portside')
	rowsGenE = getGenerador(request,'eosii', 'starboard')
	
	matrizGps = gps

	loopEosii = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'eosii':
			loopEosii.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('eosii.html', locals())

def getAlisios(request):
	
	gps = getGps(request, 'alisios')

	rowsPropB = getPropulsor(request, 'alisios', 'portside')
	rowsPropE = getPropulsor(request, 'alisios', 'starboard')
	#rowsGenB = getGenerador(request,'alisios', 'portside')
	#rowsGenE = getGenerador(request,'alisios', 'starboard')
	
	matriz = gps

	loopAlisios = []

	for i in range(len(matriz)):
		if matriz[i]['rm'] == 'alisios':
			loopAlisios.append([matriz[i]['latitud'], matriz[i]['longitud'], matriz[i]['velocidad'], matriz[i]['fechahora']])	

	return render_to_response('alisios.html', locals())
# Create your views here.
