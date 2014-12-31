from django.db import models
#Create your models here.

class Generador(models.Model):
    id = models.AutoField(primary_key=True)
    rm = models.CharField(max_length=15, blank=True)
    side = models.CharField(max_length=10, blank=True)
    fechahora = models.DateTimeField(blank=True, null=True)
    totalhours = models.FloatField(blank=True, null=True)
    triphours = models.FloatField(blank=True, null=True)
    startcounter = models.FloatField(blank=True, null=True)
    startfailurecounter = models.FloatField(blank=True, null=True)
    ch1 = models.FloatField(blank=True, null=True)
    ch2 = models.FloatField(blank=True, null=True)
    ch3 = models.FloatField(blank=True, null=True)
    ch4 = models.FloatField(blank=True, null=True)
    ch5 = models.FloatField(blank=True, null=True)
    batteryvoltage = models.FloatField(blank=True, null=True)
    fuelrate = models.FloatField(blank=True, null=True)
    rpmmeter = models.FloatField(blank=True, null=True)
    class Meta:

        db_table = 'generador'

class Gps(models.Model):
    id = models.AutoField(primary_key=True)
    rm = models.CharField(max_length=15, blank=True)
    fechahora = models.DateTimeField(blank=True, null=True)
    latitud = models.FloatField(blank=True, null=True)
    latitudns = models.CharField(db_column='latitudNS', max_length=1, blank=True) # Field name made lowercase.
    longitud = models.FloatField(blank=True, null=True)
    longitudew = models.CharField(db_column='longitudEW', max_length=1, blank=True) # Field name made lowercase.
    velocidad = models.FloatField(blank=True, null=True)
    direccion = models.FloatField(blank=True, null=True)
    pdop = models.FloatField(blank=True, null=True)
    hdop = models.FloatField(blank=True, null=True)
    class Meta:

        db_table = 'gps'

class Propulsor(models.Model):
    id = models.AutoField(primary_key=True)
    rm = models.CharField(max_length=15, blank=True)
    side = models.CharField(max_length=10, blank=True)
    fechahora = models.DateTimeField(blank=True, null=True)
    percentload = models.FloatField(blank=True, null=True)
    enginespeed = models.FloatField(blank=True, null=True)
    enginetorque = models.FloatField(blank=True, null=True)
    totalhours = models.FloatField(blank=True, null=True)
    totalfuel = models.FloatField(blank=True, null=True)
    coolanttemperature = models.FloatField(blank=True, null=True)
    fueltemperature = models.FloatField(blank=True, null=True)
    oiltemperature = models.FloatField(blank=True, null=True)
    intercoolertemperature = models.FloatField(blank=True, null=True)
    fuelpressure = models.FloatField(blank=True, null=True)
    oillevel = models.FloatField(blank=True, null=True)
    oilpressure = models.FloatField(blank=True, null=True)
    crankcasepressure2 = models.FloatField(blank=True, null=True)
    coolantlevel = models.FloatField(blank=True, null=True)
    throttleposition = models.FloatField(blank=True, null=True)
    fuelrate = models.FloatField(blank=True, null=True)
    boostpressure = models.FloatField(blank=True, null=True)
    manifoldtemperature = models.FloatField(blank=True, null=True)
    airfilterdifferentialpressure = models.FloatField(blank=True, null=True)
    exhaustgastemperature = models.FloatField(blank=True, null=True)
    electricpotentialvoltage = models.FloatField(blank=True, null=True)
    class Meta:

        db_table = 'propulsor'