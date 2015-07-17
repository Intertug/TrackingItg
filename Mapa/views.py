# Create your views here.
from django.shortcuts import render_to_response
from Mapa.models import *
from django.db import connection
from datetime import datetime, timedelta, date
from monthdelta import MonthDelta
from django.http import HttpResponse
import json

#agregar ids
remolcadores = {'ODIN': 16, 'FREY':10, 'CAREX': 5, 'MARA':13, 'APOLO':8, 'CHINOOK':32, 'ALISIOS':29, 'DON LUCHO':7, 'CRISTINA' : 6, 'KIN':27, 'TANOK':26, 'MISTRAL':28, 'VALI':23, 'BARU PACIFICO':33, 'BARU INTI':34,}
ids = { "16":'ODIN', "10":'FREY', "5": 'CAREX', "13":'MARA', "8":'APOLO', "32":'CHINOOK', "29":'ALISIOS', "7":'DON LUCHO', "6" :'CRISTINA' , "27":'KIN', "26":'TANOK', "28":'MISTRAL', "23":'VALI', "33":'BARU PACIFICO', "34":'BARU INTI',}

def getPropulsor(nom):

	cursorPropB = connection.cursor()

	cursorPropB.execute("select DataValue from [2160-DAQOnBoardData] where TimeString in (Select top 1 TimeString from [2160-DAQOnBoardData] where vesselname = '"+str(nom)+"' order by TimeString DESC) and (DataCode = 'PRP001' or DataCode = 'PRS001' or DataCode = 'PRP002' or DataCode = 'PRS002' or DataCode = 'PRP000' or DataCode = 'PRS000' or DataCode = 'PRP003' or DataCode = 'PRS003') order by DataCode desc;")

	# if 'fecha' in request.GET:
	# 	fecha = request.GET['fecha']
	# 	hora1 = request.GET['hora1']
	# 	hora2 = request.GET['hora2']
	# 	minutos1 = request.GET['minutos1']
	# 	minutos2 = request.GET['minutos2']
	# 	cursorPropB.execute("select fechahora, totalhours, totalfuel, enginespeed, percentload, fuelrate, coolanttemperature, oiltemperature, oilpressure, intercoolertemperature from propulsor where (fechahora between '" + str(fecha) + " " + str(hora1) + ":" + str(minutos1) + "' and '" + str(fecha) + " " + str(hora2) + ":" + str(minutos2) + "') and rm ='" + str(nom) + "' and side='"+ str(lado) +"' order by fechahora desc limit 1;")			
	# else:
	# 	cursorPropB.execute("select timestring, totalhours, totalfuel, enginespeed, percentload, fuelrate, coolanttemperature, oiltemperature, oilpressure, intercoolertemperature from propulsor where rm = '"+ str(nom) +"' and side='"+ str(lado) +"' order by fechahora desc limit 1;")
	# 	#cursorPropB.execute("select fechahora, totalhours, totalfuel, enginespeed, percentload, fuelrate, coolanttemperature, oiltemperature, oilpressure, intercoolertemperature from propulsor where rm = '"+ str(nom) +"' and side='"+ str(lado) +"' order by fechahora desc limit 1;")
	# #cursorPropB.execute("select fechahora, totalhours, totalfuel, enginespeed, percentload, fuelrate, coolanttemperature, oiltemperature, oilpressure, intercoolertemperature from propulsor where rm = '"+ str(nom) +"' and side='"+ str(lado) +"' and (fechahora > '2014-05-19 02:25:00' and fechahora < '2014-05-19 02:26:00');")
	rowsPropB = cursorPropB.fetchall()

	return rowsPropB

def getGenerador(nom):

	cursor = connection.cursor()

	cursor.execute("select DataValue from [2160-DAQOnBoardData] where TimeString in (Select top 1 TimeString from [2160-DAQOnBoardData] where vesselname = '"+str(nom)+"' order by TimeString DESC) and (DataCode = 'GEP001' or DataCode = 'GES001' or DataCode = 'GEP002' or DataCode = 'GES002' or DataCode = 'GEP000' or DataCode = 'GES000' or DataCode = 'GEP003' or DataCode = 'GES003') order by DataCode desc;")

	# if 'fecha' in request.GET:
	# 	fecha = request.GET['fecha']
	# 	hora1 = request.GET['hora1']
	# 	hora2 = request.GET['hora2']
	# 	minutos1 = request.GET['minutos1']
	# 	minutos2 = request.GET['minutos2']
	# 	cursor.execute("select fechahora, totalhours, triphours, startcounter, rpmmeter, ch1, ch2, ch3, ch4, ch5, batteryvoltage from generador where (fechahora between '" + str(fecha) + " " + str(hora1) + ":" + str(minutos1) + "' and '" + str(fecha) + " " + str(hora2) + ":" + str(minutos2) + "') and rm ='" + str(nom) + "' and side='"+ str(lado) +"' order by fechahora desc limit 1;")
	# else:
	# 	cursor.execute("select fechahora, totalhours, triphours, startcounter, rpmmeter, ch1, ch2, ch3, ch4, ch5, batteryvoltage from generador where rm = '"+ str(nom) +"' and side='"+ str(lado) +"' order by fechahora desc limit 1;")
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
			'fechahora': rows[i][5][:4] + "-" + rows[i][5][4:6] + "-" + rows[i][5][6:8] + " " + rows[i][5][8:10] + ":" + rows[i][5][10:12] + ":" + rows[i][5][12:14] ,
			})

	return matriz

def getGps(request, nombre):

	hoy = date.today()
	delta = timedelta(days=1)
	hoy2 = hoy + delta
	hoy = hoy.isoformat()
	hoy2 = hoy2.isoformat()
	#print hoy
	#print hoy2

	cursorGps = connection.cursor()

	if 'fecha' in request.GET:
		time = request.GET['fecha']
		hoy = datetime.strptime(time, "%Y-%m-%d")
		#print time
		#print hoy
		delta = timedelta(days=1)
		hoy2 = hoy + delta
		hoy = hoy.isoformat()[:10]
		hoy2 = hoy2.isoformat()[:10]
		#print hoy
		#print hoy2
		#hora1 = request.GET['hora1']
		#hora2 = request.GET['hora2']
		#minutos1 = request.GET['minutos1']
		#minutos2 = request.GET['minutos2']
		#cursorGps.execute("select latitud, latitudNS, longitud, longitudEW, velocidad, fechahora, rm from gps where (fechahora between '" + str(fecha) + " " + str(hora1) + ":" + str(minutos1) + "' and '" + str(fecha) + " " + str(hora2) + ":" + str(minutos2) + "') and rm ='" + str(rem) + "';")			
		cursorGps.execute("select Latitude, LatitudeNS, Longitude, LongitudeEW, Speed, TimeString, vesselname from [2150-DAQOnBoardGps] where vesselname = '"+str(nombre)+"' and TimeString > '"+str(hoy)+"' and TimeString < '"+str(hoy2)+"' order by id asc;")
	else:
		#cursorGps.execute("select latitud, latitudNS, longitud, longitudEW, velocidad, fechahora, rm from gps where (fechahora between (NOW() - CURTIME()) AND NOW()) and rm ='"+ str(rem) +"';")
		cursorGps.execute("select Latitude, LatitudeNS, Longitude, LongitudeEW, Speed, TimeString, vesselname from [2150-DAQOnBoardGps] where vesselname = '"+str(nombre)+"' and TimeString > '"+str(hoy)+"' and TimeString < '"+str(hoy2)+"' order by id asc;")

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
	cursorAlisios.execute("select top 1 Latitude, LatitudeNS, Longitude, LongitudeEW, Speed, TimeString, vesselname from [2150-DAQOnBoardGps] where vesselname = '"+str(nombre)+"' order by TimeString desc;")
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

def getColombia(request):
	
	#agregar loopRemolcador = llenarMapa('remolcador')
	loopCarex = llenarMapa('CAREX')
	loopOdin = llenarMapa('ODIN')
	loopMara = llenarMapa('MARA')
	loopApolo = llenarMapa('APOLO')
	loopChinook = llenarMapa('CHINOOK')
	loopAlisios = llenarMapa('ALISIOS')
	loopDonLucho = llenarMapa('DON LUCHO')
	loopFrey = llenarMapa('FREY')
	loopEosii = llenarMapa('EOS II')
	loopCapidahl = llenarMapa('CAPIDAHL')
	#loopBahaireII = llenarMapa('BAHAIRE II')
	#loopSirocco = llenarMapa('SIROCCO')

	return render_to_response('colombia.html', locals())

def getMexico(request):
	
	#agregar loopRemolcador = llenarMapa('remolcador')
	loopCristina = llenarMapa('CRISTINA')
	loopKin = llenarMapa('KIN')
	loopTanok = llenarMapa('TANOK')
	loopKronos = llenarMapa('KRONOS')
	loopSeatrout = llenarMapa('SEA TROUT')
	loopOceanos = llenarMapa('OCEANOS')

	return render_to_response('mexico.html', locals())

def getPeru(request):
	
	#agregar loopRemolcador = llenarMapa('remolcador')
	loopMistral = llenarMapa('MISTRAL')
	loopVali = llenarMapa('VALI')
	loopBarupacifico = llenarMapa('BARU PACIFICO')
	loopBaruInti = llenarMapa('BARU INTI')

	return render_to_response('peru.html', locals())

def getCapidahl(request):
	
	gps = getGps(request, 'CAPIDAHL')

	#rowsPropB = getPropulsor(request, 'capidahl', 'portside')
	#rowsPropE = getPropulsor(request, 'capidahl', 'starboard')
	#rowsGenB = getGenerador(request,'capidahl', 'portside')
	#rowsGenE = getGenerador(request,'capidahl', 'starboard')
	
	matrizGps = gps

	loopCapidahl = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'CAPIDAHL':
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

def getOceanos(request):
	
	gps = getGps(request, 'OCEANOS')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopOceanos = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'OCEANOS':
			loopOceanos.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('oceanos.html', locals())

def getChinook(request):
	
	gps = getGps(request, 'CHINOOK')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopChinook = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'CHINOOK':
			loopChinook.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('chinook.html', locals())

def getBahaireII(request):
	
	gps = getGps(request, 'BAHAIRE II')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopBahaireII = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'BAHAIRE II':
			loopBahaireII.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('bahaireii.html', locals())

def getBarupacifico(request):
	
	gps = getGps(request, 'BARU PACIFICO')

	rowsProp = getPropulsor('BARU PACIFICO')
	#rowsPropE = getPropulsor(request, 'barupacifico', 'starboard')
	rowsGen = getGenerador('BARU PACIFICO')
	#rowsGenE = getGenerador(request,'barupacifico', 'starboard')
	
	matrizGps = gps

	loopBarupacifico = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'BARU PACIFICO':
			loopBarupacifico.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('barupacifico.html', locals())

def getBaruInti(request):
	
	gps = getGps(request, 'BARU INTI')

	rowsProp = getPropulsor('BARU INTI')
	#rowsPropE = getPropulsor(request, 'baruinti', 'starboard')
	rowsGen = getGenerador('BARU INTI')
	#rowsGenE = getGenerador(request,'baruinti', 'starboard')
	
	matrizGps = gps

	loopBaruInti = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'BARU INTI':
			loopBaruInti.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('baruinti.html', locals())

def getMara(request):
	
	gps = getGps(request, 'MARA')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopMara = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'MARA':
			loopMara.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('mara.html', locals())

def getFrey(request):
	
	gps = getGps(request, 'FREY')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopFrey = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'FREY':
			loopFrey.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('frey.html', locals())

def getDonLucho(request):
	
	gps = getGps(request, 'DON LUCHO')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopDonLucho = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'DON LUCHO':
			loopDonLucho.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('donlucho.html', locals())

def getApolo(request):
	
	gps = getGps(request, 'APOLO')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopApolo = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'APOLO':
			loopApolo.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('apolo.html', locals())

def getOdin(request):
	
	gps = getGps(request, 'ODIN')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopOdin = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'ODIN':
			loopOdin.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('odin.html', locals())

def getVali(request):
	
	gps = getGps(request, 'VALI')

	rowsProp = getPropulsor('VALI')
	#rowsPropE = getPropulsor(request, 'vali', 'starboard')
	rowsGen = getGenerador('VALI')
	#rowsGenE = getGenerador(request,'vali', 'starboard')
	
	matrizGps = gps

	loopVali = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'VALI':
			loopVali.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('vali.html', locals())

def getKronos(request):
	
	gps = getGps(request, 'KRONOS')

	#rowsProp = getPropulsor('CRISTINA')
	#rowsPropE = getPropulsor(request, 'vali', 'starboard')
	#rowsGen = getGenerador('CRISTINA')
	#rowsGenE = getGenerador(request,'vali', 'starboard')
	
	matrizGps = gps

	loopKronos = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'KRONOS':
			loopKronos.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('kronos.html', locals())

def getCristina(request):
	
	gps = getGps(request, 'CRISTINA')

	#rowsProp = getPropulsor('CRISTINA')
	#rowsPropE = getPropulsor(request, 'vali', 'starboard')
	#rowsGen = getGenerador('CRISTINA')
	#rowsGenE = getGenerador(request,'vali', 'starboard')
	
	matrizGps = gps

	loopCristina = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'CRISTINA':
			loopCristina.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('cristina.html', locals())

def getCarex(request):
	
	gps = getGps(request, 'CAREX')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopCarex = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'CAREX':
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
	
	gps = getGps(request, 'SIROCCO')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopSirocco = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'SIROCCO':
			loopSirocco.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('sirocco.html', locals())

def getTanok(request):
	
	gps = getGps(request, 'TANOK')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopTanok = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'TANOK':
			loopTanok.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('tanok.html', locals())

def getSeatrout(request):
	
	gps = getGps(request, 'SEA TROUT')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopSeatrout = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'SEA TROUT':
			loopSeatrout.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('seatrout.html', locals())

def getKin(request):
	
	gps = getGps(request, 'KIN')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopKin = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'KIN':
			loopKin.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('kin.html', locals())

def getTitania(request):
	
	gps = getGps(request, 'TITANIA')

	#rowsPropB = getPropulsor(request, 'mistral', 'portside')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	#rowsGenB = getGenerador(request,'mistral', 'portside')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopTitania = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'TITANIA':
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
	
	gps = getGps(request, 'MISTRAL')

	rowsProp = getPropulsor('MISTRAL')
	#rowsPropE = getPropulsor(request, 'mistral', 'starboard')
	rowsGen = getGenerador('MISTRAL')
	#rowsGenE = getGenerador(request,'mistral', 'starboard')
	
	matrizGps = gps

	loopMistral = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'MISTRAL':
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
	
	gps = getGps(request, 'EOS II')

	#rowsPropB = getPropulsor(request, 'eosii', 'portside')
	#rowsPropE = getPropulsor(request, 'eosii', 'starboard')
	#rowsGenB = getGenerador(request,'eosii', 'portside')
	#rowsGenE = getGenerador(request,'eosii', 'starboard')
	
	matrizGps = gps

	loopEosii = []

	for i in range(len(matrizGps)):
		if matrizGps[i]['rm'] == 'EOS II':
			loopEosii.append([matrizGps[i]['latitud'], matrizGps[i]['longitud'], matrizGps[i]['velocidad'], matrizGps[i]['fechahora']])

	return render_to_response('eosii.html', locals())

def getAlisios(request):
	
	gps = getGps(request, 'ALISIOS')

	#rowsProp = getPropulsor('ALISIOS')
	#rowsProp = getPropulsor(request, 'alisios', 'starboard')
	#rowsGen = getGenerador('ALISIOS')
	#rowsGenE = getGenerador(request,'alisios', 'starboard')
	
	matriz = gps

	loopAlisios = []

	for i in range(len(matriz)):
		if matriz[i]['rm'] == 'ALISIOS':
			loopAlisios.append([matriz[i]['latitud'], matriz[i]['longitud'], matriz[i]['velocidad'], matriz[i]['fechahora']])	

	return render_to_response('alisios.html', locals())
# Create your views here.

def posicion(request):

	barcos = ('ODIN', 'CAREX', 'MARA', 'APOLO', 'CHINOOK', 'ALISIOS', 'DON LUCHO', 'CRISTINA', 'KIN', 'TANOK', 'MISTRAL', 'VALI', 'BARU PACIFICO', 'BARU INTI',)
	
	data = {
    "clusterGrid": 60,
    "vessels": [],
	}

	for i in range(len(barcos)):

		matriz = llenarMapa(barcos[i])

		vessels = [
		        {
		            "veseelID": remolcadores[barcos[i]],
		            "position": {
		                "value": {
		                    "lat": matriz[0],
		                    "lon": matriz[1]
		                },
		                "label": "Posicion"
		            },
		            "speed": {
		                "value": matriz[2],
		                "label": "Velocidad"
		            },
		            "engine": [
		                {
		                    "type": "propulsion",
		                    "code": "FR54",
		                    "location": "center",
		                    "dayhours": {
		                        "value": 82,
		                        "label": "Horas de uso"
		                    },
		                    "dayfuel": {
		                        "value": 200,
		                        "label": "Combustible consumido"
		                    },
		                    "maxrpm": {
		                        "value": 1200,
		                        "label": "RPM Maximo"
		                    },
		                    "maxfuelrate": {
		                        "value": 201,
		                        "label": "Maximo consumo por hora"
		                    }
		                }
		            ]
		        }
		    ]

		data['vessels'] += vessels

	json_data = json.dumps(data)

	return HttpResponse(json_data, content_type='application/json')

def recorrido(request):


	gps = getGps(request, ids[str(request.GET["vessel"])])

	data = {
		"vesselID": str(request.GET["vessel"]),
		"coordenates" : [],
	}
	
	for i in range(len(gps)):

		alert = False
		if gps[i]['velocidad'] > 8:
			alert = True

		point = [

		    {
            	"position": {
                	"value": {
                    	"lat": gps[i]['latitud'],
                    	"lon": gps[i]['longitud']
                	},
                	"label": "Posicion"
            	},
            	"speed": {
                	"value": gps[i]['velocidad'],
                	"label": "Velocidad"
            	},
            	"datetime": {
                	"value": gps[i]['fechahora'],
                	"label": "Fecha"
            	},
            	"alert": alert
        	}
		]

		data["coordenates"] += point

	json_data = json.dumps(data)

	return HttpResponse(json_data, content_type='application/json')
