# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class 0001Configuration(models.Model):
    paramtype = models.TextField(db_column='ParamType') # Field name made lowercase.
    paramname = models.TextField(db_column='ParamName') # Field name made lowercase.
    paramvalue = models.TextField(db_column='ParamValue') # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    class Meta:
        db_table = '0001-Configuration'

class 0005Sysapp(models.Model):
    uid = models.TextField()
    appcode = models.CharField(max_length=20, db_column='AppCode') # Field name made lowercase.
    description = models.CharField(max_length=128, db_column='Description') # Field name made lowercase.
    accesstype = models.SmallIntegerField(db_column='AccessType') # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status') # Field name made lowercase.
    params = models.CharField(max_length=1024, db_column='Params') # Field name made lowercase.
    class Meta:
        db_table = '0005-SysApp'

class 0010Sysdevices(models.Model):
    uid = models.TextField()
    devicecode = models.CharField(max_length=20, db_column='DeviceCode') # Field name made lowercase.
    description = models.CharField(max_length=128, db_column='Description') # Field name made lowercase.
    devicetype = models.SmallIntegerField(db_column='DeviceType') # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status') # Field name made lowercase.
    params = models.CharField(max_length=1024, db_column='Params') # Field name made lowercase.
    class Meta:
        db_table = '0010-SysDevices'

class 0020Versioning(models.Model):
    objectcode = models.CharField(max_length=50, db_column='ObjectCode') # Field name made lowercase.
    objectversion = models.CharField(max_length=14, db_column='ObjectVersion') # Field name made lowercase.
    description = models.CharField(max_length=128, db_column='Description') # Field name made lowercase.
    lastupdate = models.CharField(max_length=16, db_column='LastUpdate') # Field name made lowercase.
    class Meta:
        db_table = '0020-Versioning'

class 0030Sysjobs(models.Model):
    uid = models.TextField()
    jobtype = models.TextField(db_column='JobType') # Field name made lowercase.
    jobstatus = models.TextField(db_column='JobStatus') # Field name made lowercase.
    jobname = models.TextField(db_column='JobName') # Field name made lowercase.
    description = models.TextField(db_column='Description') # Field name made lowercase.
    jobstage = models.SmallIntegerField(db_column='JobStage') # Field name made lowercase.
    conndata = models.TextField(db_column='ConnData') # Field name made lowercase.
    sqldata = models.TextField(db_column='SqlData') # Field name made lowercase.
    userdata = models.TextField(db_column='UserData') # Field name made lowercase.
    returndata = models.TextField(db_column='ReturnData') # Field name made lowercase.
    priority = models.SmallIntegerField(db_column='Priority') # Field name made lowercase.
    schedule = models.TextField(db_column='Schedule') # Field name made lowercase.
    creationdate = models.TextField(db_column='CreationDate') # Field name made lowercase.
    initdate = models.TextField(db_column='InitDate') # Field name made lowercase.
    enddate = models.TextField(db_column='EndDate') # Field name made lowercase.
    lastrun = models.TextField(db_column='LastRun') # Field name made lowercase.
    class Meta:
        db_table = '0030-SysJobs'

class 0050Users(models.Model):
    uid = models.TextField()
    username = models.CharField(max_length=32)
    userpassword = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    usergroup = models.CharField(max_length=20)
    userlevel = models.SmallIntegerField()
    userstatus = models.SmallIntegerField()
    creationdate = models.CharField(max_length=16)
    enddate = models.CharField(max_length=16)
    firstname = models.CharField(max_length=32, db_column='FirstName') # Field name made lowercase.
    lastname = models.CharField(max_length=32, db_column='LastName') # Field name made lowercase.
    iddocument = models.CharField(max_length=20, db_column='IdDocument') # Field name made lowercase.
    address = models.CharField(max_length=50, db_column='Address') # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityId') # Field name made lowercase.
    cityname = models.CharField(max_length=50, db_column='CityName') # Field name made lowercase.
    country = models.CharField(max_length=2, db_column='Country') # Field name made lowercase.
    phone = models.CharField(max_length=20, db_column='Phone') # Field name made lowercase.
    position = models.CharField(max_length=50, db_column='Position') # Field name made lowercase.
    subsidiary = models.CharField(max_length=50, db_column='Subsidiary') # Field name made lowercase.
    employeeid = models.IntegerField(db_column='EmployeeID') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '0050-Users'

class 0052Profiles(models.Model):
    uid = models.TextField()
    appuid = models.CharField(max_length=36, db_column='AppUID') # Field name made lowercase.
    profiletype = models.SmallIntegerField(db_column='ProfileType') # Field name made lowercase.
    deviceuid = models.CharField(max_length=36, db_column='DeviceUID') # Field name made lowercase.
    useruid = models.CharField(max_length=36, db_column='UserUID') # Field name made lowercase.
    vesseluid = models.CharField(max_length=36, db_column='VesselUID') # Field name made lowercase.
    accesslevel = models.CharField(max_length=128, db_column='AccessLevel') # Field name made lowercase.
    locationcode = models.CharField(max_length=128, db_column='LocationCode') # Field name made lowercase.
    infotagcode = models.CharField(max_length=128, db_column='InfoTagCode') # Field name made lowercase.
    creationdate = models.CharField(max_length=16, db_column='CreationDate') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State') # Field name made lowercase.
    preferedlang = models.CharField(max_length=2, db_column='PreferedLang') # Field name made lowercase.
    menuspec = models.CharField(max_length=1024, db_column='MenuSpec') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0052-Profiles'

class 0055Sessions(models.Model):
    uid = models.TextField()
    appuid = models.CharField(max_length=36, db_column='AppUID') # Field name made lowercase.
    profileuid = models.CharField(max_length=36, db_column='ProfileUID') # Field name made lowercase.
    useruid = models.CharField(max_length=36, db_column='UserUID') # Field name made lowercase.
    deviceuid = models.CharField(max_length=36, db_column='DeviceUID') # Field name made lowercase.
    vesseluid = models.CharField(max_length=36, db_column='VesselUID') # Field name made lowercase.
    accesslevel = models.CharField(max_length=128, db_column='AccessLevel') # Field name made lowercase.
    locationcode = models.CharField(max_length=128, db_column='LocationCode') # Field name made lowercase.
    infotagcode = models.CharField(max_length=128, db_column='InfoTagCode') # Field name made lowercase.
    remoteinfo = models.CharField(max_length=64, db_column='RemoteInfo') # Field name made lowercase.
    initdate = models.CharField(max_length=16, db_column='InitDate') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '0055-Sessions'

class 0060Appsmenuspecs(models.Model):
    appuid = models.CharField(max_length=36, db_column='AppUID') # Field name made lowercase.
    speccode = models.CharField(max_length=32, db_column='SpecCode') # Field name made lowercase.
    specdata = models.CharField(max_length=1024, db_column='SpecData') # Field name made lowercase.
    itemtype = models.SmallIntegerField(db_column='ItemType') # Field name made lowercase.
    langcode = models.CharField(max_length=2, db_column='LangCode') # Field name made lowercase.
    objectversion = models.CharField(max_length=14, db_column='ObjectVersion') # Field name made lowercase.
    description = models.CharField(max_length=128, db_column='Description') # Field name made lowercase.
    lastupdate = models.CharField(max_length=16, db_column='LastUpdate') # Field name made lowercase.
    class Meta:
        db_table = '0060-AppsMenuSpecs'

class 0065Appsentities(models.Model):
    entityname = models.CharField(max_length=64, db_column='EntityName') # Field name made lowercase.
    appuid = models.CharField(max_length=36, db_column='AppUID') # Field name made lowercase.
    entitytable = models.CharField(max_length=64, db_column='EntityTable') # Field name made lowercase.
    accessdata = models.CharField(max_length=256, db_column='AccessData') # Field name made lowercase.
    locationdata = models.CharField(max_length=256, db_column='LocationData') # Field name made lowercase.
    additionaldata = models.CharField(max_length=512, db_column='AdditionalData') # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State') # Field name made lowercase.
    class Meta:
        db_table = '0065-AppsEntities'

class 0080Tasks(models.Model):
    id = models.AutoField()
    class Meta:
        db_table = '0080-Tasks'

class 0082Taskslogs(models.Model):
    id = models.AutoField()
    class Meta:
        db_table = '0082-TasksLogs'

class 0090Activitiesclasses(models.Model):
    uid = models.TextField()
    description = models.CharField(max_length=3072, db_column='Description') # Field name made lowercase.
    triggerentity = models.CharField(max_length=64, db_column='TriggerEntity') # Field name made lowercase.
    triggervalue = models.CharField(max_length=256, db_column='TriggerValue') # Field name made lowercase.
    accesslevel = models.CharField(max_length=128, db_column='AccessLevel') # Field name made lowercase.
    locationcode = models.CharField(max_length=128, db_column='LocationCode') # Field name made lowercase.
    activityclassinfo = models.CharField(max_length=128, db_column='ActivityClassInfo') # Field name made lowercase.
    creationdate = models.CharField(max_length=16, db_column='CreationDate') # Field name made lowercase.
    initdate = models.CharField(max_length=16, db_column='InitDate') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State') # Field name made lowercase.
    class Meta:
        db_table = '0090-ActivitiesClasses'

class 0091Activitiesclassesnodes(models.Model):
    uid = models.TextField()
    activityuid = models.CharField(max_length=36, db_column='ActivityUID') # Field name made lowercase.
    description = models.CharField(max_length=3072, db_column='Description') # Field name made lowercase.
    nodecode = models.CharField(max_length=32, db_column='NodeCode') # Field name made lowercase.
    nodetype = models.SmallIntegerField(db_column='NodeType') # Field name made lowercase.
    accesslevel = models.CharField(max_length=128, db_column='AccessLevel') # Field name made lowercase.
    locationcode = models.CharField(max_length=128, db_column='LocationCode') # Field name made lowercase.
    nodeclassinfo = models.CharField(max_length=256, db_column='NodeClassInfo') # Field name made lowercase.
    nodeuiinfo = models.CharField(max_length=256, db_column='NodeUIInfo') # Field name made lowercase.
    nodebranch = models.CharField(max_length=256, db_column='NodeBranch') # Field name made lowercase.
    nextnodeinfo = models.CharField(max_length=256, db_column='NextNodeInfo') # Field name made lowercase.
    nextnodedesc = models.CharField(max_length=3072, db_column='NextNodeDesc') # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State') # Field name made lowercase.
    class Meta:
        db_table = '0091-ActivitiesClassesNodes'

class 0092Activitiesclassesnodesui(models.Model):
    partcode = models.CharField(max_length=32, db_column='PartCode') # Field name made lowercase.
    description = models.CharField(max_length=1024, db_column='Description') # Field name made lowercase.
    template = models.CharField(max_length=1024, db_column='Template') # Field name made lowercase.
    langcode = models.CharField(max_length=2, db_column='LangCode') # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State') # Field name made lowercase.
    class Meta:
        db_table = '0092-ActivitiesClassesNodesUI'

class 0095Activitiesobjects(models.Model):
    uid = models.CharField(max_length=36)
    activityclassuid = models.CharField(max_length=36, db_column='ActivityClassUID') # Field name made lowercase.
    description = models.CharField(max_length=1024, db_column='Description') # Field name made lowercase.
    entity = models.CharField(max_length=64, db_column='Entity') # Field name made lowercase.
    entityuid = models.CharField(max_length=36, db_column='EntityUID') # Field name made lowercase.
    relatedentities = models.CharField(max_length=128, db_column='RelatedEntities') # Field name made lowercase.
    accesslevel = models.CharField(max_length=128, db_column='AccessLevel') # Field name made lowercase.
    locationcode = models.CharField(max_length=128, db_column='LocationCode') # Field name made lowercase.
    activityinfo = models.CharField(max_length=128, db_column='ActivityInfo') # Field name made lowercase.
    initdate = models.CharField(max_length=16, db_column='InitDate') # Field name made lowercase.
    initsession = models.CharField(max_length=36, db_column='InitSession') # Field name made lowercase.
    currentnodeinfo = models.CharField(max_length=256, db_column='CurrentNodeInfo') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    endsession = models.CharField(max_length=36, db_column='EndSession') # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State') # Field name made lowercase.
    class Meta:
        db_table = '0095-ActivitiesObjects'

class 0096Activitiesobjectsnodes(models.Model):
    uid = models.CharField(max_length=36)
    activityuid = models.CharField(max_length=36, db_column='ActivityUID') # Field name made lowercase.
    nodeclassuid = models.CharField(max_length=36, db_column='NodeClassUID') # Field name made lowercase.
    description = models.CharField(max_length=1024, db_column='Description') # Field name made lowercase.
    nodenum = models.SmallIntegerField(db_column='NodeNum') # Field name made lowercase.
    nodecode = models.CharField(max_length=32, db_column='NodeCode') # Field name made lowercase.
    nodetype = models.SmallIntegerField(db_column='NodeType') # Field name made lowercase.
    accesslevel = models.CharField(max_length=128, db_column='AccessLevel') # Field name made lowercase.
    locationcode = models.CharField(max_length=128, db_column='LocationCode') # Field name made lowercase.
    nodeinfo = models.CharField(max_length=512, db_column='NodeInfo') # Field name made lowercase.
    nodeuiinfo = models.CharField(max_length=1024, db_column='NodeUIInfo') # Field name made lowercase.
    nodevalues = models.CharField(max_length=1024, db_column='NodeValues') # Field name made lowercase.
    initdate = models.CharField(max_length=16, db_column='InitDate') # Field name made lowercase.
    initsession = models.CharField(max_length=36, db_column='InitSession') # Field name made lowercase.
    previousnode = models.CharField(max_length=36, db_column='PreviousNode') # Field name made lowercase.
    nextnodedesc = models.CharField(max_length=1024, db_column='NextNodeDesc') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    endsession = models.CharField(max_length=36, db_column='EndSession') # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State') # Field name made lowercase.
    class Meta:
        db_table = '0096-ActivitiesObjectsNodes'

class 0120Locations(models.Model):
    descriptioncode = models.CharField(max_length=16, db_column='DescriptionCode') # Field name made lowercase.
    description = models.CharField(max_length=64, db_column='Description') # Field name made lowercase.
    locationname = models.CharField(max_length=64, db_column='LocationName') # Field name made lowercase.
    continent = models.SmallIntegerField(db_column='Continent') # Field name made lowercase.
    country = models.CharField(max_length=2, db_column='Country') # Field name made lowercase.
    region = models.IntegerField(db_column='Region') # Field name made lowercase.
    city = models.IntegerField(db_column='City') # Field name made lowercase.
    office = models.IntegerField(db_column='Office') # Field name made lowercase.
    port = models.IntegerField(db_column='Port') # Field name made lowercase.
    terminal = models.IntegerField(db_column='Terminal') # Field name made lowercase.
    dock = models.IntegerField(db_column='Dock') # Field name made lowercase.
    locationcode = models.CharField(max_length=64, db_column='LocationCode') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    class Meta:
        db_table = '0120-Locations'

class 0130Locationslog(models.Model):
    locationid = models.IntegerField(db_column='LocationId') # Field name made lowercase.
    labourtype = models.SmallIntegerField(db_column='LabourType') # Field name made lowercase.
    logtype = models.SmallIntegerField(db_column='LogType') # Field name made lowercase.
    initdate = models.CharField(max_length=16, db_column='InitDate') # Field name made lowercase.
    initsession = models.CharField(max_length=36, db_column='InitSession') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    endsession = models.CharField(max_length=36, db_column='EndSession') # Field name made lowercase.
    deviceuid = models.CharField(max_length=36, db_column='DeviceUID') # Field name made lowercase.
    vesseluid = models.CharField(max_length=36, db_column='VesselUID') # Field name made lowercase.
    loginfo = models.CharField(max_length=64, db_column='LogInfo') # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State') # Field name made lowercase.
    class Meta:
        db_table = '0130-LocationsLog'

class 0220Vessels(models.Model):
    uid = models.TextField()
    vesselcode = models.CharField(max_length=4)
    vesselname = models.CharField(max_length=50)
    imo = models.CharField(max_length=15, db_column='IMO') # Field name made lowercase.
    functionsinfo = models.CharField(max_length=128, db_column='FunctionsInfo') # Field name made lowercase.
    shipyardid = models.IntegerField(db_column='ShipyardID') # Field name made lowercase.
    vesselmodel = models.CharField(max_length=16, db_column='VesselModel') # Field name made lowercase.
    classificationid = models.IntegerField(db_column='ClassificationID') # Field name made lowercase.
    classdescription = models.CharField(max_length=64, db_column='ClassDescription') # Field name made lowercase.
    vesseltypeid = models.IntegerField(db_column='VesselTypeID') # Field name made lowercase.
    vesseltypeinfo = models.CharField(max_length=50, db_column='VesselTypeInfo') # Field name made lowercase.
    ownerid = models.IntegerField(db_column='OwnerID') # Field name made lowercase.
    flagid = models.IntegerField(db_column='FlagID') # Field name made lowercase.
    yearofbuilt = models.IntegerField(db_column='YearOfBuilt') # Field name made lowercase.
    length = models.DecimalField(decimal_places=0, max_digits=18, db_column='Length') # Field name made lowercase.
    beam = models.DecimalField(decimal_places=0, max_digits=18, db_column='Beam') # Field name made lowercase.
    draught = models.DecimalField(decimal_places=0, max_digits=18, db_column='Draught') # Field name made lowercase.
    grt = models.DecimalField(decimal_places=0, max_digits=18, db_column='GRT') # Field name made lowercase.
    enginebuilderid = models.IntegerField(db_column='EngineBuilderID') # Field name made lowercase.
    engineinfo = models.CharField(max_length=128, db_column='EngineInfo') # Field name made lowercase.
    totalpower = models.IntegerField(db_column='TotalPower') # Field name made lowercase.
    maxrpm = models.IntegerField(db_column='MaxRPM') # Field name made lowercase.
    bollardpull = models.DecimalField(decimal_places=0, max_digits=18, db_column='BollardPull') # Field name made lowercase.
    speed = models.DecimalField(decimal_places=0, max_digits=18, db_column='Speed') # Field name made lowercase.
    fueloil = models.IntegerField(db_column='FuelOil') # Field name made lowercase.
    freshwater = models.DecimalField(decimal_places=0, max_digits=18, db_column='FreshWater') # Field name made lowercase.
    gensetinfo = models.CharField(max_length=64, db_column='GensetInfo') # Field name made lowercase.
    towinginfo = models.CharField(max_length=64, db_column='TowingInfo') # Field name made lowercase.
    fifiinfo = models.CharField(max_length=64, db_column='FifiInfo') # Field name made lowercase.
    deckspace = models.IntegerField(db_column='DeckSpace') # Field name made lowercase.
    accountinginfo = models.CharField(max_length=32, db_column='AccountingInfo') # Field name made lowercase.
    supplychaininfo = models.CharField(max_length=64, db_column='SupplyChainInfo') # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId') # Field name made lowercase.
    locationcode = models.CharField(max_length=128, db_column='LocationCode') # Field name made lowercase.
    labourtype = models.SmallIntegerField(db_column='LabourType') # Field name made lowercase.
    syncinfocode = models.CharField(max_length=16, db_column='SyncInfoCode') # Field name made lowercase.
    customname1 = models.CharField(max_length=50, db_column='CustomName1') # Field name made lowercase.
    newscode = models.CharField(max_length=32, db_column='NewsCode') # Field name made lowercase.
    equipcode = models.CharField(max_length=32, db_column='EquipCode') # Field name made lowercase.
    autogendocsnews = models.SmallIntegerField(db_column='AutogenDocsNews') # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0220-Vessels'

class 0224Vesselstanks(models.Model):
    vesseluid = models.CharField(max_length=36, db_column='VesselUID') # Field name made lowercase.
    tankuid = models.CharField(max_length=36, db_column='TankUID') # Field name made lowercase.
    tankcode = models.CharField(max_length=16, db_column='TankCode') # Field name made lowercase.
    contenttype = models.SmallIntegerField(db_column='ContentType') # Field name made lowercase.
    contenttypename = models.CharField(max_length=16, db_column='ContentTypeName') # Field name made lowercase.
    tankdescription = models.CharField(max_length=32, db_column='TankDescription') # Field name made lowercase.
    tankcolor = models.CharField(max_length=7, db_column='TankColor') # Field name made lowercase.
    lastupdate = models.CharField(max_length=16, db_column='LastUpdate') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0224-VesselsTanks'

class 0225Vesselstankscapacity(models.Model):
    vesseluid = models.CharField(max_length=36, db_column='VesselUID') # Field name made lowercase.
    tankuid = models.CharField(max_length=36, db_column='TankUID') # Field name made lowercase.
    tankcode = models.CharField(max_length=16, db_column='TankCode') # Field name made lowercase.
    trim = models.FloatField(db_column='Trim') # Field name made lowercase.
    sounding = models.FloatField(db_column='Sounding') # Field name made lowercase.
    volumen = models.FloatField(db_column='Volumen') # Field name made lowercase.
    weight = models.FloatField(db_column='Weight') # Field name made lowercase.
    vcg = models.FloatField(db_column='Vcg') # Field name made lowercase.
    tcg = models.FloatField(db_column='Tcg') # Field name made lowercase.
    lcg = models.FloatField(db_column='Lcg') # Field name made lowercase.
    fsm_t = models.FloatField(db_column='Fsm_T') # Field name made lowercase.
    lastupdate = models.CharField(max_length=16, db_column='LastUpdate') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0225-VesselsTanksCapacity'

class 0400Assetsonboard(models.Model):
    vesseluid = models.CharField(max_length=36, db_column='VesselUID') # Field name made lowercase.
    vesselaccountingcode = models.CharField(max_length=5, db_column='VesselAccountingCode') # Field name made lowercase.
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    assetname = models.CharField(max_length=64, db_column='AssetName') # Field name made lowercase.
    typeid = models.SmallIntegerField(db_column='TypeID') # Field name made lowercase.
    systemcode = models.CharField(max_length=8, db_column='SystemCode') # Field name made lowercase.
    groupcode = models.CharField(max_length=8, db_column='GroupCode') # Field name made lowercase.
    functioncode = models.CharField(max_length=8, db_column='FunctionCode') # Field name made lowercase.
    assetnumbercode = models.CharField(max_length=8, db_column='AssetNumberCode') # Field name made lowercase.
    subsystemcode = models.CharField(max_length=8, db_column='SubsystemCode') # Field name made lowercase.
    status = models.CharField(max_length=4, db_column='Status') # Field name made lowercase.
    description = models.CharField(max_length=255, db_column='Description') # Field name made lowercase.
    location = models.CharField(max_length=255, db_column='Location') # Field name made lowercase.
    criticality = models.SmallIntegerField(db_column='Criticality') # Field name made lowercase.
    generatetoa = models.SmallIntegerField(db_column='GenerateTOA') # Field name made lowercase.
    lastupdate = models.CharField(max_length=16, db_column='LastUpdate') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0400-AssetsOnBoard'

class 0401Assetssystems(models.Model):
    systemcode = models.CharField(max_length=16, db_column='SystemCode') # Field name made lowercase.
    systemname = models.CharField(max_length=64, db_column='SystemName') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    langcode = models.CharField(max_length=2, db_column='LangCode') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0401-AssetsSystems'

class 0402Assetsgroups(models.Model):
    groupcode = models.CharField(max_length=8, db_column='GroupCode') # Field name made lowercase.
    functioncode = models.CharField(max_length=8, db_column='FunctionCode') # Field name made lowercase.
    functionname = models.CharField(max_length=64, db_column='FunctionName') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    langcode = models.CharField(max_length=2, db_column='LangCode') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0402-AssetsGroups'

class 0403Assetssubsystems(models.Model):
    groupcode = models.CharField(max_length=8, db_column='GroupCode') # Field name made lowercase.
    subsystemcode = models.CharField(max_length=8, db_column='SubsystemCode') # Field name made lowercase.
    subsystemname = models.CharField(max_length=64, db_column='SubsystemName') # Field name made lowercase.
    langcode = models.CharField(max_length=2, db_column='LangCode') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0403-AssetsSubsystems'

class 0404Componentsonboard(models.Model):
    componentcode = models.CharField(max_length=20, db_column='ComponentCode') # Field name made lowercase.
    componentname = models.CharField(max_length=50, db_column='ComponentName') # Field name made lowercase.
    typeid = models.IntegerField(db_column='TypeID') # Field name made lowercase.
    vesselid = models.IntegerField(db_column='VesselID') # Field name made lowercase.
    systemid = models.IntegerField(db_column='SystemID') # Field name made lowercase.
    equipmentid = models.IntegerField(db_column='EquipmentID') # Field name made lowercase.
    subsystemid = models.IntegerField(db_column='SubsystemID') # Field name made lowercase.
    componentid = models.IntegerField(db_column='ComponentID') # Field name made lowercase.
    componentsubid1 = models.IntegerField(db_column='ComponentSubID1') # Field name made lowercase.
    componentsubid2 = models.IntegerField(db_column='ComponentSubID2') # Field name made lowercase.
    componentsubid3 = models.IntegerField(db_column='ComponentSubID3') # Field name made lowercase.
    status = models.CharField(max_length=4, db_column='Status') # Field name made lowercase.
    description = models.CharField(max_length=255, db_column='Description') # Field name made lowercase.
    location = models.CharField(max_length=255, db_column='Location') # Field name made lowercase.
    criticality = models.SmallIntegerField(db_column='Criticality') # Field name made lowercase.
    generatetoa = models.SmallIntegerField(db_column='GenerateTOA') # Field name made lowercase.
    lastupdate = models.CharField(max_length=16, db_column='LastUpdate') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0404-ComponentsOnBoard'

class 0405Onboardreftypes(models.Model):
    typeclass = models.CharField(max_length=8, db_column='TypeClass') # Field name made lowercase.
    typecode = models.CharField(max_length=10, db_column='TypeCode') # Field name made lowercase.
    langcode = models.CharField(max_length=2, db_column='LangCode') # Field name made lowercase.
    typename = models.CharField(max_length=256, db_column='TypeName') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    relateddata = models.CharField(max_length=256, db_column='RelatedData') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0405-OnBoardRefTypes'

class 0406Generalreftypes(models.Model):
    typeclass = models.CharField(max_length=8, db_column='TypeClass') # Field name made lowercase.
    typecode = models.CharField(max_length=64, db_column='TypeCode') # Field name made lowercase.
    langcode = models.CharField(max_length=2, db_column='LangCode') # Field name made lowercase.
    typename = models.CharField(max_length=256, db_column='TypeName') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    relateddata = models.CharField(max_length=256, db_column='RelatedData') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0406-GeneralRefTypes'

class 0407Mobilereftypes(models.Model):
    typeclass = models.CharField(max_length=64, db_column='TypeClass') # Field name made lowercase.
    typecode = models.CharField(max_length=10, db_column='TypeCode') # Field name made lowercase.
    langcode = models.CharField(max_length=2, db_column='LangCode') # Field name made lowercase.
    typename = models.CharField(max_length=256, db_column='TypeName') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    description = models.CharField(max_length=256, db_column='Description') # Field name made lowercase.
    relateddata = models.CharField(max_length=256, db_column='RelatedData') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0407-MobileRefTypes'

class 0410Hsetrialsdata(models.Model):
    datatype = models.SmallIntegerField(db_column='DataType') # Field name made lowercase.
    numorder = models.SmallIntegerField(db_column='NumOrder') # Field name made lowercase.
    captiontext = models.CharField(max_length=128, db_column='CaptionText') # Field name made lowercase.
    additional = models.CharField(max_length=128, db_column='Additional') # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State') # Field name made lowercase.
    langcode = models.CharField(max_length=2, db_column='LangCode') # Field name made lowercase.
    locationcode = models.CharField(max_length=64, db_column='LocationCode') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0410-HSETrialsData'

class 0420Goodsonboard(models.Model):
    segment = models.CharField(max_length=10, db_column='Segment') # Field name made lowercase.
    family = models.CharField(max_length=10, db_column='Family') # Field name made lowercase.
    class_field = models.CharField(max_length=10, db_column='Class') # Field name made lowercase. Field renamed because it was a Python reserved word.
    impaclassid = models.IntegerField(db_column='IMPAClassID') # Field name made lowercase.
    commodity = models.CharField(max_length=10, db_column='Commodity') # Field name made lowercase.
    extension = models.CharField(max_length=4, db_column='Extension') # Field name made lowercase.
    code = models.CharField(max_length=15, db_column='Code') # Field name made lowercase.
    description = models.CharField(max_length=255, db_column='Description') # Field name made lowercase.
    descriptionlang = models.CharField(max_length=2, db_column='DescriptionLang') # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryID') # Field name made lowercase.
    unitid = models.IntegerField(db_column='UnitID') # Field name made lowercase.
    mode = models.SmallIntegerField(db_column='Mode') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    lastupdate = models.CharField(max_length=16, db_column='LastUpdate') # Field name made lowercase.
    locationcode = models.CharField(max_length=64, db_column='LocationCode') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0420-GoodsOnBoard'

class 0422Unspsconboard(models.Model):
    codetype = models.SmallIntegerField(db_column='CodeType') # Field name made lowercase.
    code = models.CharField(max_length=10, db_column='Code') # Field name made lowercase.
    title = models.CharField(max_length=128, db_column='Title') # Field name made lowercase.
    titlelang = models.CharField(max_length=2, db_column='TitleLang') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0422-UNSPSCOnBoard'

class 0424Goodscategories(models.Model):
    categoryname = models.CharField(max_length=128, db_column='CategoryName') # Field name made lowercase.
    langcode = models.CharField(max_length=2, db_column='LangCode') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0424-GoodsCategories'

class 0450Periodicdocuments(models.Model):
    documentcode = models.CharField(max_length=16, db_column='DocumentCode') # Field name made lowercase.
    doctype = models.SmallIntegerField(db_column='DocType') # Field name made lowercase.
    documentname = models.CharField(max_length=64, db_column='DocumentName') # Field name made lowercase.
    doccriticity = models.SmallIntegerField(db_column='DocCriticity') # Field name made lowercase.
    daystorequest = models.IntegerField(db_column='DaysToRequest') # Field name made lowercase.
    daystoendorse = models.IntegerField(db_column='DaysToEndorse') # Field name made lowercase.
    expirationperiod = models.IntegerField(db_column='ExpirationPeriod') # Field name made lowercase.
    endorseperiod = models.IntegerField(db_column='EndorsePeriod') # Field name made lowercase.
    authority = models.CharField(max_length=128, db_column='Authority') # Field name made lowercase.
    observations = models.CharField(max_length=255, db_column='Observations') # Field name made lowercase.
    locationcode = models.CharField(max_length=128)
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0450-PeriodicDocuments'

class 0455Documentsonboard(models.Model):
    uid = models.TextField()
    vesseluid = models.CharField(max_length=36, db_column='VesselUID') # Field name made lowercase.
    documentcode = models.CharField(max_length=16, db_column='DocumentCode') # Field name made lowercase.
    documentname = models.CharField(max_length=64, db_column='DocumentName') # Field name made lowercase.
    releasedate = models.CharField(max_length=10, db_column='ReleaseDate') # Field name made lowercase.
    expiredate = models.CharField(max_length=10, db_column='ExpireDate') # Field name made lowercase.
    endorsedate = models.CharField(max_length=10, db_column='EndorseDate') # Field name made lowercase.
    documentstatus = models.SmallIntegerField(db_column='DocumentStatus') # Field name made lowercase.
    observations = models.CharField(max_length=255, db_column='Observations') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0455-DocumentsOnBoard'

class 0500Assetsonmobile(models.Model):
    vesseluid = models.CharField(max_length=36, db_column='VesselUID') # Field name made lowercase.
    vesselaccountingcode = models.CharField(max_length=5, db_column='VesselAccountingCode') # Field name made lowercase.
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    assetname = models.CharField(max_length=64, db_column='AssetName') # Field name made lowercase.
    typeid = models.SmallIntegerField(db_column='TypeID') # Field name made lowercase.
    systemcode = models.CharField(max_length=8, db_column='SystemCode') # Field name made lowercase.
    groupcode = models.CharField(max_length=3, db_column='GroupCode') # Field name made lowercase.
    functioncode = models.CharField(max_length=3, db_column='FunctionCode') # Field name made lowercase.
    assetnumbercode = models.CharField(max_length=3, db_column='AssetNumberCode') # Field name made lowercase.
    subsystemcode = models.CharField(max_length=3, db_column='SubsystemCode') # Field name made lowercase.
    status = models.CharField(max_length=4, db_column='Status') # Field name made lowercase.
    description = models.CharField(max_length=255, db_column='Description') # Field name made lowercase.
    assetmark = models.CharField(max_length=64, db_column='AssetMark') # Field name made lowercase.
    assetmodel = models.CharField(max_length=64, db_column='AssetModel') # Field name made lowercase.
    location = models.CharField(max_length=255, db_column='Location') # Field name made lowercase.
    criticality = models.SmallIntegerField(db_column='Criticality') # Field name made lowercase.
    generatetoa = models.SmallIntegerField(db_column='GenerateTOA') # Field name made lowercase.
    lastupdate = models.CharField(max_length=16, db_column='LastUpdate') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0500-AssetsOnMobile'

class 0510Mobileroutineclasses(models.Model):
    uid = models.CharField(max_length=36)
    vesseluid = models.CharField(max_length=36, db_column='VesselUID') # Field name made lowercase.
    routinecode = models.CharField(max_length=16, db_column='RoutineCode') # Field name made lowercase.
    routinetitle = models.CharField(max_length=64, db_column='RoutineTitle') # Field name made lowercase.
    description = models.CharField(max_length=64, db_column='Description') # Field name made lowercase.
    routinetype = models.SmallIntegerField(db_column='RoutineType') # Field name made lowercase.
    frequencytype = models.SmallIntegerField(db_column='FrequencyType') # Field name made lowercase.
    frequencydata = models.CharField(max_length=16, db_column='FrequencyData') # Field name made lowercase.
    accumulationtype = models.SmallIntegerField(db_column='AccumulationType') # Field name made lowercase.
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    lastupdate = models.CharField(max_length=16, db_column='LastUpdate') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0510-MobileRoutineClasses'

class 0512Mobileroutineactivitiesclasses(models.Model):
    uid = models.CharField(max_length=36)
    routineclassuid = models.CharField(max_length=36, db_column='RoutineClassUID') # Field name made lowercase.
    vesseluid = models.CharField(max_length=36, db_column='VesselUID') # Field name made lowercase.
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    activitycode = models.CharField(max_length=16, db_column='ActivityCode') # Field name made lowercase.
    activitytitle = models.CharField(max_length=64, db_column='ActivityTitle') # Field name made lowercase.
    description = models.CharField(max_length=64, db_column='Description') # Field name made lowercase.
    vesselstate = models.SmallIntegerField(db_column='VesselState') # Field name made lowercase.
    assetstate = models.SmallIntegerField(db_column='AssetState') # Field name made lowercase.
    maintenancetype = models.SmallIntegerField(db_column='MaintenanceType') # Field name made lowercase.
    datatype = models.SmallIntegerField(db_column='DataType') # Field name made lowercase.
    datatypelistitems = models.CharField(max_length=512, db_column='DataTypeListItems') # Field name made lowercase.
    variablename = models.CharField(max_length=32, db_column='VariableName') # Field name made lowercase.
    variableunit = models.SmallIntegerField(db_column='VariableUnit') # Field name made lowercase.
    unitname = models.CharField(max_length=32, db_column='UnitName') # Field name made lowercase.
    lowerlimit = models.CharField(max_length=32, db_column='LowerLimit') # Field name made lowercase.
    upperlimit = models.CharField(max_length=32, db_column='UpperLimit') # Field name made lowercase.
    warningmessage = models.CharField(max_length=1024, db_column='WarningMessage') # Field name made lowercase.
    lastupdate = models.CharField(max_length=16, db_column='LastUpdate') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '0512-MobileRoutineActivitiesClasses'

class 1111Crewonboard(models.Model):
    uid = models.TextField()
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    personuid = models.CharField(max_length=36, db_column='PersonUID') # Field name made lowercase.
    persondocument = models.CharField(max_length=32, db_column='PersonDocument') # Field name made lowercase.
    personname = models.CharField(max_length=64, db_column='PersonName') # Field name made lowercase.
    personlastname = models.CharField(max_length=64, db_column='PersonLastName') # Field name made lowercase.
    persontitleid = models.IntegerField(db_column='PersonTitleId') # Field name made lowercase.
    persontitlename = models.CharField(max_length=64, db_column='PersonTitleName') # Field name made lowercase.
    personchargeid = models.IntegerField(db_column='PersonChargeId') # Field name made lowercase.
    personchargename = models.CharField(max_length=64, db_column='PersonChargeName') # Field name made lowercase.
    onboardfromdate = models.CharField(max_length=10, db_column='OnBoardFromDate') # Field name made lowercase.
    onboardtodate = models.CharField(max_length=10, db_column='OnBoardToDate') # Field name made lowercase.
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    closesession = models.CharField(max_length=36)
    closedate = models.CharField(max_length=16)
    closereason = models.SmallIntegerField()
    status = models.SmallIntegerField(db_column='Status') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=128, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1111-CrewOnBoard'

class 1200Onboardworks(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    worktypeid = models.IntegerField(db_column='WorkTypeId') # Field name made lowercase.
    worktypename = models.CharField(max_length=128, db_column='WorkTypeName') # Field name made lowercase.
    sailorscount = models.SmallIntegerField(db_column='SailorsCount') # Field name made lowercase.
    workdate = models.CharField(max_length=10, db_column='WorkDate') # Field name made lowercase.
    inithour = models.CharField(max_length=5, db_column='InitHour') # Field name made lowercase.
    endhour = models.CharField(max_length=5, db_column='EndHour') # Field name made lowercase.
    observations = models.CharField(max_length=1024, db_column='Observations') # Field name made lowercase.
    class Meta:
        db_table = '1200-OnBoardWorks'

class 1205Onboardtofe(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    tofereportdate = models.CharField(max_length=10, db_column='TOFEReportDate') # Field name made lowercase.
    tofegenerated = models.SmallIntegerField(db_column='TOFEGenerated') # Field name made lowercase.
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    assetname = models.CharField(max_length=64, db_column='AssetName') # Field name made lowercase.
    tofeoriginid = models.IntegerField(db_column='TOFEOriginId') # Field name made lowercase.
    tofeoriginname = models.CharField(max_length=128, db_column='TOFEOriginName') # Field name made lowercase.
    newsinfo = models.CharField(max_length=64, db_column='NewsInfo') # Field name made lowercase.
    workorderinfo = models.CharField(max_length=64, db_column='WorkOrderInfo') # Field name made lowercase.
    tofedate = models.CharField(max_length=10, db_column='TOFEDate') # Field name made lowercase.
    tofeinithour = models.CharField(max_length=5, db_column='TOFEInitHour') # Field name made lowercase.
    tofeendhour = models.CharField(max_length=5, db_column='TOFEEndHour') # Field name made lowercase.
    toagenerated = models.SmallIntegerField(db_column='TOAGenerated') # Field name made lowercase.
    toadate = models.CharField(max_length=10, db_column='TOADate') # Field name made lowercase.
    toainithour = models.CharField(max_length=5, db_column='TOAInitHour') # Field name made lowercase.
    toaendhour = models.CharField(max_length=5, db_column='TOAEndHour') # Field name made lowercase.
    observations = models.CharField(max_length=1024, db_column='Observations') # Field name made lowercase.
    class Meta:
        db_table = '1205-OnBoardTOFE'

class 1210Onboardnews(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    code = models.CharField(max_length=50, db_column='Code') # Field name made lowercase.
    process = models.SmallIntegerField(db_column='Process') # Field name made lowercase.
    processname = models.CharField(max_length=128, db_column='ProcessName') # Field name made lowercase.
    newtype = models.SmallIntegerField(db_column='NewType') # Field name made lowercase.
    typename = models.CharField(max_length=128, db_column='TypeName') # Field name made lowercase.
    newclass = models.SmallIntegerField(db_column='NewClass') # Field name made lowercase.
    classname = models.CharField(max_length=128, db_column='ClassName') # Field name made lowercase.
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    assetname = models.CharField(max_length=128, db_column='AssetName') # Field name made lowercase.
    event = models.CharField(max_length=1024, db_column='Event') # Field name made lowercase.
    cause = models.CharField(max_length=1024, db_column='Cause') # Field name made lowercase.
    effect = models.CharField(max_length=1024, db_column='Effect') # Field name made lowercase.
    eventdate = models.CharField(max_length=16, db_column='EventDate') # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status') # Field name made lowercase.
    statusname = models.CharField(max_length=128, db_column='StatusName') # Field name made lowercase.
    criticality = models.SmallIntegerField(db_column='Criticality') # Field name made lowercase.
    criticalityname = models.CharField(max_length=128, db_column='CriticalityName') # Field name made lowercase.
    reportername = models.CharField(max_length=128, db_column='ReporterName') # Field name made lowercase.
    reportercharge = models.SmallIntegerField(db_column='ReporterCharge') # Field name made lowercase.
    reporterchargename = models.CharField(max_length=64, db_column='ReporterChargeName') # Field name made lowercase.
    newupddate = models.CharField(max_length=16, db_column='NewUpdDate') # Field name made lowercase.
    newclosedate = models.CharField(max_length=16, db_column='NewCloseDate') # Field name made lowercase.
    newcompleteddate = models.CharField(max_length=16, db_column='NewCompletedDate') # Field name made lowercase.
    currentactivityuid = models.CharField(max_length=36, db_column='CurrentActivityUID') # Field name made lowercase.
    currentactivitydesc = models.CharField(max_length=128, db_column='CurrentActivityDesc') # Field name made lowercase.
    currentactivitydate = models.CharField(max_length=16, db_column='CurrentActivityDate') # Field name made lowercase.
    nextactivitydesc = models.CharField(max_length=128, db_column='NextActivityDesc') # Field name made lowercase.
    lastqualityvalue = models.SmallIntegerField(db_column='LastQualityValue') # Field name made lowercase.
    attachmentcode = models.CharField(max_length=128, db_column='AttachmentCode') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=128, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1210-OnBoardNews'

class 1215Onboardnewslog(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    logtype = models.SmallIntegerField(db_column='LogType') # Field name made lowercase.
    loguser = models.CharField(max_length=36, db_column='LogUser') # Field name made lowercase.
    logusername = models.CharField(max_length=64, db_column='LogUserName') # Field name made lowercase.
    logdata = models.CharField(max_length=128, db_column='LogData') # Field name made lowercase.
    comment = models.CharField(max_length=1024, db_column='Comment') # Field name made lowercase.
    class Meta:
        db_table = '1215-OnBoardNewsLog'

class 1220Onboardservsreq(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    assetname = models.CharField(max_length=128, db_column='AssetName') # Field name made lowercase.
    assetsubsystem = models.CharField(max_length=10, db_column='AssetSubsystem') # Field name made lowercase.
    subsystemname = models.CharField(max_length=128, db_column='SubsystemName') # Field name made lowercase.
    event = models.CharField(max_length=3072, db_column='Event') # Field name made lowercase.
    eventdate = models.CharField(max_length=16, db_column='EventDate') # Field name made lowercase.
    requiredwork = models.CharField(max_length=1024, db_column='RequiredWork') # Field name made lowercase.
    conditions = models.CharField(max_length=512, db_column='Conditions') # Field name made lowercase.
    horometer = models.CharField(max_length=64, db_column='Horometer') # Field name made lowercase.
    assetreference = models.CharField(max_length=64, db_column='AssetReference') # Field name made lowercase.
    assetstatus = models.SmallIntegerField(db_column='AssetStatus') # Field name made lowercase.
    statusname = models.CharField(max_length=128, db_column='StatusName') # Field name made lowercase.
    assetcriticality = models.SmallIntegerField(db_column='AssetCriticality') # Field name made lowercase.
    autonomous = models.SmallIntegerField(db_column='Autonomous') # Field name made lowercase.
    lastqualityvalue = models.SmallIntegerField(db_column='LastQualityValue') # Field name made lowercase.
    approvalstatus = models.SmallIntegerField(db_column='ApprovalStatus') # Field name made lowercase.
    approvaldate = models.CharField(max_length=16, db_column='ApprovalDate') # Field name made lowercase.
    approvalsessionuid = models.CharField(max_length=36, db_column='ApprovalSessionUID') # Field name made lowercase.
    approvaluser = models.CharField(max_length=128, db_column='ApprovalUser') # Field name made lowercase.
    senttoeamstatus = models.SmallIntegerField(db_column='SentToEamStatus') # Field name made lowercase.
    senttoeamdate = models.CharField(max_length=16, db_column='SentToEamDate') # Field name made lowercase.
    eamassignedcode = models.CharField(max_length=64, db_column='EamAssignedCode') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1220-OnBoardServsReq'

class 1222Onboardopsservsreq(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    servicecodeid = models.SmallIntegerField(db_column='ServiceCodeId') # Field name made lowercase.
    servicename = models.CharField(max_length=128, db_column='ServiceName') # Field name made lowercase.
    event = models.CharField(max_length=1024, db_column='Event') # Field name made lowercase.
    eventdate = models.CharField(max_length=16, db_column='EventDate') # Field name made lowercase.
    requiredwork = models.CharField(max_length=1024, db_column='RequiredWork') # Field name made lowercase.
    reqstatus = models.SmallIntegerField(db_column='ReqStatus') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=256, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1222-OnBoardOpsServsReq'

class 1224Onboardticservsreq(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    assetname = models.CharField(max_length=128, db_column='AssetName') # Field name made lowercase.
    event = models.CharField(max_length=1024, db_column='Event') # Field name made lowercase.
    eventdate = models.CharField(max_length=16, db_column='EventDate') # Field name made lowercase.
    requiredwork = models.CharField(max_length=1024, db_column='RequiredWork') # Field name made lowercase.
    assetreference = models.CharField(max_length=64, db_column='AssetReference') # Field name made lowercase.
    assetstatus = models.SmallIntegerField(db_column='AssetStatus') # Field name made lowercase.
    statusname = models.CharField(max_length=128, db_column='StatusName') # Field name made lowercase.
    reqstatus = models.SmallIntegerField(db_column='ReqStatus') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=256, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1224-OnBoardTicServsReq'

class 1225Onboardgoodsreq(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    itemcount = models.SmallIntegerField(db_column='ItemCount') # Field name made lowercase.
    reqstatus = models.SmallIntegerField(db_column='ReqStatus') # Field name made lowercase.
    infoquality = models.SmallIntegerField(db_column='InfoQuality') # Field name made lowercase.
    approvalmode = models.SmallIntegerField(db_column='ApprovalMode') # Field name made lowercase.
    approvaldate = models.CharField(max_length=16, db_column='ApprovalDate') # Field name made lowercase.
    approvalsessionuid = models.CharField(max_length=36, db_column='ApprovalSessionUID') # Field name made lowercase.
    approvaluser = models.CharField(max_length=128, db_column='ApprovalUser') # Field name made lowercase.
    senttoeamstatus = models.SmallIntegerField(db_column='SentToEamStatus') # Field name made lowercase.
    senttoeamdate = models.CharField(max_length=16, db_column='SentToEamDate') # Field name made lowercase.
    eamassignedcode = models.CharField(max_length=64, db_column='EamAssignedCode') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1225-OnBoardGoodsReq'

class 1227Onboardgoodsreqdetail(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    requid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    itemnumber = models.SmallIntegerField(db_column='ItemNumber') # Field name made lowercase.
    itemcode = models.CharField(max_length=20, db_column='ItemCode') # Field name made lowercase.
    itemcategory = models.IntegerField(db_column='ItemCategory') # Field name made lowercase.
    itemcategoryname = models.CharField(max_length=128, db_column='ItemCategoryName') # Field name made lowercase.
    itemname = models.CharField(max_length=128, db_column='ItemName') # Field name made lowercase.
    adddescription = models.CharField(max_length=256, db_column='AddDescription') # Field name made lowercase.
    itemunit = models.IntegerField(db_column='ItemUnit') # Field name made lowercase.
    itemunitname = models.CharField(max_length=128, db_column='ItemUnitName') # Field name made lowercase.
    itemquant = models.SmallIntegerField(db_column='ItemQuant') # Field name made lowercase.
    approvedquant = models.SmallIntegerField(db_column='ApprovedQuant') # Field name made lowercase.
    receivedquant = models.SmallIntegerField(db_column='ReceivedQuant') # Field name made lowercase.
    comment = models.CharField(max_length=1024, db_column='Comment') # Field name made lowercase.
    reqstatus = models.SmallIntegerField(db_column='ReqStatus') # Field name made lowercase.
    eamassignedcode = models.CharField(max_length=64, db_column='EamAssignedCode') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1227-OnBoardGoodsReqDetail'

class 1230Onboardhsetrials(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    trialtype = models.SmallIntegerField(db_column='TrialType') # Field name made lowercase.
    trialname = models.CharField(max_length=128, db_column='TrialName') # Field name made lowercase.
    trialdate = models.CharField(max_length=10, db_column='TrialDate') # Field name made lowercase.
    trialmonth = models.SmallIntegerField(db_column='TrialMonth') # Field name made lowercase.
    participants = models.CharField(max_length=1024, db_column='Participants') # Field name made lowercase.
    activitytime01 = models.CharField(max_length=5, db_column='ActivityTime01') # Field name made lowercase.
    activitytime02 = models.CharField(max_length=5, db_column='ActivityTime02') # Field name made lowercase.
    activitytime03 = models.CharField(max_length=5, db_column='ActivityTime03') # Field name made lowercase.
    activitytime04 = models.CharField(max_length=5, db_column='ActivityTime04') # Field name made lowercase.
    activitytime05 = models.CharField(max_length=5, db_column='ActivityTime05') # Field name made lowercase.
    activitytime06 = models.CharField(max_length=5, db_column='ActivityTime06') # Field name made lowercase.
    secuenceinfo1 = models.CharField(max_length=2048, db_column='SecuenceInfo1') # Field name made lowercase.
    secuenceinfo2 = models.CharField(max_length=2048, db_column='SecuenceInfo2') # Field name made lowercase.
    secuenceinfo3 = models.CharField(max_length=2048, db_column='SecuenceInfo3') # Field name made lowercase.
    conclusionsinfo1 = models.CharField(max_length=2048, db_column='ConclusionsInfo1') # Field name made lowercase.
    conclusionsinfo2 = models.CharField(max_length=2048, db_column='ConclusionsInfo2') # Field name made lowercase.
    infoquality = models.SmallIntegerField(db_column='InfoQuality') # Field name made lowercase.
    approvalmode = models.SmallIntegerField(db_column='ApprovalMode') # Field name made lowercase.
    approvaldate = models.CharField(max_length=16, db_column='ApprovalDate') # Field name made lowercase.
    approvalsessionuid = models.CharField(max_length=36, db_column='ApprovalSessionUID') # Field name made lowercase.
    approvaluser = models.CharField(max_length=128, db_column='ApprovalUser') # Field name made lowercase.
    class Meta:
        db_table = '1230-OnBoardHSETrials'

class 1232Onboardhseevent(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    event = models.CharField(max_length=1024, db_column='Event') # Field name made lowercase.
    eventdate = models.CharField(max_length=16, db_column='EventDate') # Field name made lowercase.
    eventtype = models.SmallIntegerField(db_column='EventType') # Field name made lowercase.
    eventname = models.CharField(max_length=128, db_column='EventName') # Field name made lowercase.
    standards = models.CharField(max_length=1024, db_column='Standards') # Field name made lowercase.
    hseplan = models.CharField(max_length=1024, db_column='HsePlan') # Field name made lowercase.
    causes = models.CharField(max_length=2048, db_column='Causes') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=256, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1232-OnBoardHSEEvent'

class 1235Onboardhsereports(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    repuser = models.CharField(max_length=36, db_column='RepUser') # Field name made lowercase.
    event = models.CharField(max_length=1024, db_column='Event') # Field name made lowercase.
    eventdate = models.CharField(max_length=16, db_column='EventDate') # Field name made lowercase.
    reportdetail = models.CharField(max_length=2048, db_column='ReportDetail') # Field name made lowercase.
    situation = models.SmallIntegerField(db_column='Situation') # Field name made lowercase.
    infoquality = models.SmallIntegerField(db_column='InfoQuality') # Field name made lowercase.
    approvalmode = models.SmallIntegerField(db_column='ApprovalMode') # Field name made lowercase.
    approvaldate = models.CharField(max_length=16, db_column='ApprovalDate') # Field name made lowercase.
    approvalsessionuid = models.CharField(max_length=36, db_column='ApprovalSessionUID') # Field name made lowercase.
    approvaluser = models.CharField(max_length=128, db_column='ApprovalUser') # Field name made lowercase.
    class Meta:
        db_table = '1235-OnBoardHSEReports'

class 1240Onboardhseactions(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    actiontype = models.SmallIntegerField(db_column='ActionType') # Field name made lowercase.
    typename = models.CharField(max_length=128, db_column='TypeName') # Field name made lowercase.
    process = models.SmallIntegerField(db_column='Process') # Field name made lowercase.
    processname = models.CharField(max_length=128, db_column='ProcessName') # Field name made lowercase.
    reportername = models.CharField(max_length=128, db_column='ReporterName') # Field name made lowercase.
    reportercharge = models.CharField(max_length=128, db_column='ReporterCharge') # Field name made lowercase.
    controlperson = models.CharField(max_length=128, db_column='ControlPerson') # Field name made lowercase.
    controlcharge = models.CharField(max_length=128, db_column='ControlCharge') # Field name made lowercase.
    incidentdate = models.CharField(max_length=16, db_column='IncidentDate') # Field name made lowercase.
    incidentplace = models.CharField(max_length=128, db_column='IncidentPlace') # Field name made lowercase.
    event = models.CharField(max_length=1024, db_column='Event') # Field name made lowercase.
    improvement = models.CharField(max_length=1024, db_column='Improvement') # Field name made lowercase.
    inmediatecause = models.CharField(max_length=1024, db_column='InmediateCause') # Field name made lowercase.
    realcause = models.CharField(max_length=1024, db_column='RealCause') # Field name made lowercase.
    injuredname = models.CharField(max_length=128, db_column='InjuredName') # Field name made lowercase.
    injuredcharge = models.CharField(max_length=128, db_column='InjuredCharge') # Field name made lowercase.
    injuredregional = models.CharField(max_length=128, db_column='InjuredRegional') # Field name made lowercase.
    injuredpart = models.CharField(max_length=128, db_column='InjuredPart') # Field name made lowercase.
    injurednature = models.CharField(max_length=128, db_column='InjuredNature') # Field name made lowercase.
    injureddays = models.SmallIntegerField(db_column='InjuredDays') # Field name made lowercase.
    injuredcause = models.CharField(max_length=128, db_column='InjuredCause') # Field name made lowercase.
    damagearea = models.CharField(max_length=128, db_column='DamageArea') # Field name made lowercase.
    damagenature = models.CharField(max_length=128, db_column='DamageNature') # Field name made lowercase.
    damageestcost = models.IntegerField(db_column='DamageEstCost') # Field name made lowercase.
    damagerealcost = models.IntegerField(db_column='DamageRealCost') # Field name made lowercase.
    damagecause = models.CharField(max_length=128, db_column='DamageCause') # Field name made lowercase.
    damageobservation = models.CharField(max_length=128, db_column='DamageObservation') # Field name made lowercase.
    infoquality = models.SmallIntegerField(db_column='InfoQuality') # Field name made lowercase.
    approvalmode = models.SmallIntegerField(db_column='ApprovalMode') # Field name made lowercase.
    approvaldate = models.CharField(max_length=16, db_column='ApprovalDate') # Field name made lowercase.
    approvalsessionuid = models.CharField(max_length=36, db_column='ApprovalSessionUID') # Field name made lowercase.
    approvaluser = models.CharField(max_length=128, db_column='ApprovalUser') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1240-OnBoardHSEActions'

class 1242Onboardhseservsreq(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    assetname = models.CharField(max_length=128, db_column='AssetName') # Field name made lowercase.
    reqtype = models.SmallIntegerField(db_column='ReqType') # Field name made lowercase.
    reqname = models.CharField(max_length=128, db_column='ReqName') # Field name made lowercase.
    expdate = models.CharField(max_length=16, db_column='ExpDate') # Field name made lowercase.
    event = models.CharField(max_length=1024, db_column='Event') # Field name made lowercase.
    eventdate = models.CharField(max_length=16, db_column='EventDate') # Field name made lowercase.
    requiredwork = models.CharField(max_length=1024, db_column='RequiredWork') # Field name made lowercase.
    assetreference = models.CharField(max_length=64, db_column='AssetReference') # Field name made lowercase.
    assetstatus = models.SmallIntegerField(db_column='AssetStatus') # Field name made lowercase.
    statusname = models.CharField(max_length=128, db_column='StatusName') # Field name made lowercase.
    reqstatus = models.SmallIntegerField(db_column='ReqStatus') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=256, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1242-OnBoardHseServsReq'

class 1245Onboardwrkdrestrep(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    reporttype = models.SmallIntegerField(db_column='ReportType') # Field name made lowercase.
    typename = models.CharField(max_length=128, db_column='TypeName') # Field name made lowercase.
    period = models.CharField(max_length=50, db_column='Period') # Field name made lowercase.
    peoplecount = models.SmallIntegerField(db_column='PeopleCount') # Field name made lowercase.
    infoquality = models.SmallIntegerField(db_column='InfoQuality') # Field name made lowercase.
    approvalmode = models.SmallIntegerField(db_column='ApprovalMode') # Field name made lowercase.
    approvaldate = models.CharField(max_length=16, db_column='ApprovalDate') # Field name made lowercase.
    approvalsessionuid = models.CharField(max_length=36, db_column='ApprovalSessionUID') # Field name made lowercase.
    approvaluser = models.CharField(max_length=128, db_column='ApprovalUser') # Field name made lowercase.
    senttoeamstatus = models.SmallIntegerField(db_column='SentToEamStatus') # Field name made lowercase.
    senttoeamdate = models.CharField(max_length=16, db_column='SentToEamDate') # Field name made lowercase.
    eamassignedcode = models.CharField(max_length=64, db_column='EamAssignedCode') # Field name made lowercase.
    processstatus = models.SmallIntegerField(db_column='ProcessStatus') # Field name made lowercase.
    processdate = models.CharField(max_length=16, db_column='ProcessDate') # Field name made lowercase.
    legalizedate = models.CharField(max_length=16, db_column='LegalizeDate') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1245-OnBoardWrkdRestRep'

class 1247Onboardwrkdrestrepdet(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    requid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    personnumber = models.SmallIntegerField(db_column='PersonNumber') # Field name made lowercase.
    personname = models.CharField(max_length=128, db_column='PersonName') # Field name made lowercase.
    persondocument = models.CharField(max_length=32, db_column='PersonDocument') # Field name made lowercase.
    normalinit = models.CharField(max_length=16, db_column='NormalInit') # Field name made lowercase.
    normalend = models.CharField(max_length=16, db_column='NormalEnd') # Field name made lowercase.
    addinit = models.CharField(max_length=16, db_column='AddInit') # Field name made lowercase.
    addend = models.CharField(max_length=16, db_column='AddEnd') # Field name made lowercase.
    restinit = models.CharField(max_length=16, db_column='RestInit') # Field name made lowercase.
    restend = models.CharField(max_length=16, db_column='RestEnd') # Field name made lowercase.
    comment = models.CharField(max_length=1024, db_column='Comment') # Field name made lowercase.
    legalizedate = models.CharField(max_length=16, db_column='LegalizeDate') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1247-OnBoardWrkdRestRepDet'

class 1250Onboardvacationreq(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    repuser = models.CharField(max_length=36, db_column='RepUser') # Field name made lowercase.
    name = models.CharField(max_length=50, db_column='Name') # Field name made lowercase.
    lastname = models.CharField(max_length=50, db_column='LastName') # Field name made lowercase.
    iddocument = models.CharField(max_length=25, db_column='IDDocument') # Field name made lowercase.
    charge = models.CharField(max_length=50, db_column='Charge') # Field name made lowercase.
    initdate = models.CharField(max_length=16, db_column='InitDate') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    fromdate = models.CharField(max_length=16, db_column='FromDate') # Field name made lowercase.
    infoquality = models.SmallIntegerField(db_column='InfoQuality') # Field name made lowercase.
    approvalmode = models.SmallIntegerField(db_column='ApprovalMode') # Field name made lowercase.
    approvaldate = models.CharField(max_length=16, db_column='ApprovalDate') # Field name made lowercase.
    approvalsessionuid = models.CharField(max_length=36, db_column='ApprovalSessionUID') # Field name made lowercase.
    approvaluser = models.CharField(max_length=128, db_column='ApprovalUser') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1250-OnBoardVacationReq'

class 1252Onboardpeoplenew(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    peoplecount = models.SmallIntegerField(db_column='PeopleCount') # Field name made lowercase.
    processstatus = models.SmallIntegerField(db_column='ProcessStatus') # Field name made lowercase.
    processdate = models.CharField(max_length=16, db_column='ProcessDate') # Field name made lowercase.
    legalizedate = models.CharField(max_length=16, db_column='LegalizeDate') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=128, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1252-OnBoardPeopleNew'

class 1254Onboardpeoplenewdet(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    requid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    personnumber = models.SmallIntegerField(db_column='PersonNumber') # Field name made lowercase.
    personname = models.CharField(max_length=128, db_column='PersonName') # Field name made lowercase.
    persondocument = models.CharField(max_length=32, db_column='PersonDocument') # Field name made lowercase.
    personcharge = models.CharField(max_length=32, db_column='PersonCharge') # Field name made lowercase.
    personnewtype = models.SmallIntegerField(db_column='PersonNewType') # Field name made lowercase.
    typename = models.CharField(max_length=128, db_column='TypeName') # Field name made lowercase.
    newdays = models.SmallIntegerField(db_column='NewDays') # Field name made lowercase.
    comment = models.CharField(max_length=1024, db_column='Comment') # Field name made lowercase.
    legalizedate = models.CharField(max_length=16, db_column='LegalizeDate') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=128, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1254-OnBoardPeopleNewDet'

class 1255Onboardnavreport(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    repuser = models.CharField(max_length=36, db_column='RepUser') # Field name made lowercase.
    reason = models.CharField(max_length=512, db_column='Reason') # Field name made lowercase.
    origin = models.CharField(max_length=100, db_column='Origin') # Field name made lowercase.
    initdate = models.CharField(max_length=16, db_column='InitDate') # Field name made lowercase.
    destination = models.CharField(max_length=100, db_column='Destination') # Field name made lowercase.
    arrivaldate = models.CharField(max_length=16, db_column='ArrivalDate') # Field name made lowercase.
    daysonport = models.SmallIntegerField(db_column='DaysOnPort') # Field name made lowercase.
    destdeparturedate = models.CharField(max_length=16, db_column='DestDepartureDate') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    peoplecount = models.SmallIntegerField(db_column='PeopleCount') # Field name made lowercase.
    infoquality = models.SmallIntegerField(db_column='InfoQuality') # Field name made lowercase.
    approvalmode = models.SmallIntegerField(db_column='ApprovalMode') # Field name made lowercase.
    approvaldate = models.CharField(max_length=16, db_column='ApprovalDate') # Field name made lowercase.
    approvalsessionuid = models.CharField(max_length=36, db_column='ApprovalSessionUID') # Field name made lowercase.
    approvaluser = models.CharField(max_length=128, db_column='ApprovalUser') # Field name made lowercase.
    processstatus = models.SmallIntegerField(db_column='ProcessStatus') # Field name made lowercase.
    processdate = models.CharField(max_length=16, db_column='ProcessDate') # Field name made lowercase.
    legalizedate = models.CharField(max_length=16, db_column='LegalizeDate') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1255-OnBoardNavReport'

class 1257Onboardnavreportdetail(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    repuid = models.CharField(max_length=36)
    repuser = models.CharField(max_length=36, db_column='RepUser') # Field name made lowercase.
    personnumber = models.SmallIntegerField(db_column='PersonNumber') # Field name made lowercase.
    personname = models.CharField(max_length=128, db_column='PersonName') # Field name made lowercase.
    initdate = models.CharField(max_length=16, db_column='InitDate') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    legalizedate = models.CharField(max_length=16, db_column='LegalizeDate') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=1024, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1257-OnBoardNavReportDetail'

class 1260Onboardopsevent(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    eventtypeid = models.IntegerField(db_column='EventTypeId') # Field name made lowercase.
    eventtypename = models.CharField(max_length=128, db_column='EventTypeName') # Field name made lowercase.
    regquantity = models.CharField(max_length=16, db_column='RegQuantity') # Field name made lowercase.
    eventdate = models.CharField(max_length=10, db_column='EventDate') # Field name made lowercase.
    inithour = models.CharField(max_length=5, db_column='InitHour') # Field name made lowercase.
    endhour = models.CharField(max_length=5, db_column='EndHour') # Field name made lowercase.
    observations = models.CharField(max_length=1024, db_column='Observations') # Field name made lowercase.
    class Meta:
        db_table = '1260-OnBoardOpsEvent'

class 1265Onboardworkorders(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    ordernumber = models.IntegerField(db_column='OrderNumber') # Field name made lowercase.
    vessellocationid = models.IntegerField(db_column='VesselLocationId') # Field name made lowercase.
    proceduretype = models.SmallIntegerField(db_column='ProcedureType') # Field name made lowercase.
    eventdate = models.CharField(max_length=10, db_column='EventDate') # Field name made lowercase.
    clientship = models.CharField(max_length=64, db_column='ClientShip') # Field name made lowercase.
    shiptype = models.SmallIntegerField(db_column='ShipType') # Field name made lowercase.
    shipgrt = models.IntegerField(db_column='ShipGRT') # Field name made lowercase.
    shiplength = models.IntegerField(db_column='ShipLength') # Field name made lowercase.
    shipdwt = models.IntegerField(db_column='ShipDWT') # Field name made lowercase.
    clientlineid = models.IntegerField(db_column='ClientLineId') # Field name made lowercase.
    clientagencyid = models.IntegerField(db_column='ClientAgencyId') # Field name made lowercase.
    shipcaptain = models.CharField(max_length=64, db_column='ShipCaptain') # Field name made lowercase.
    pilotdata = models.CharField(max_length=128, db_column='PilotData') # Field name made lowercase.
    pushposid = models.SmallIntegerField(db_column='PushPosId') # Field name made lowercase.
    callhour = models.CharField(max_length=5, db_column='CallHour') # Field name made lowercase.
    standbyhour = models.CharField(max_length=5, db_column='StandbyHour') # Field name made lowercase.
    inithour = models.CharField(max_length=5, db_column='InitHour') # Field name made lowercase.
    endhour = models.CharField(max_length=5, db_column='EndHour') # Field name made lowercase.
    addsupport = models.CharField(max_length=1024, db_column='AddSupport') # Field name made lowercase.
    observations = models.CharField(max_length=1024, db_column='Observations') # Field name made lowercase.
    associateddata = models.CharField(max_length=256, db_column='AssociatedData') # Field name made lowercase.
    class Meta:
        db_table = '1265-OnBoardWorkOrders'

class 1280Onboardperiodicservs(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    servicetype = models.SmallIntegerField(db_column='ServiceType') # Field name made lowercase.
    servicename = models.CharField(max_length=128, db_column='ServiceName') # Field name made lowercase.
    eventdate = models.CharField(max_length=10, db_column='EventDate') # Field name made lowercase.
    observations = models.CharField(max_length=1024, db_column='Observations') # Field name made lowercase.
    reqstatus = models.SmallIntegerField(db_column='ReqStatus') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=256, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1280-OnBoardPeriodicServs'

class 1285Onboardexpireddocs(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    newuid = models.CharField(max_length=36)
    requser = models.CharField(max_length=36, db_column='ReqUser') # Field name made lowercase.
    documentuid = models.CharField(max_length=36, db_column='DocumentUid') # Field name made lowercase.
    documentname = models.CharField(max_length=64, db_column='DocumentName') # Field name made lowercase.
    eventdate = models.CharField(max_length=16, db_column='EventDate') # Field name made lowercase.
    requestdate = models.CharField(max_length=10, db_column='RequestDate') # Field name made lowercase.
    releasedate = models.CharField(max_length=10, db_column='ReleaseDate') # Field name made lowercase.
    expirydate = models.CharField(max_length=10, db_column='ExpiryDate') # Field name made lowercase.
    observations = models.CharField(max_length=1024, db_column='Observations') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=256, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1285-OnBoardExpiredDocs'

class 1300Onboarddocuments(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    documenttype = models.SmallIntegerField(db_column='DocumentType') # Field name made lowercase.
    documentname = models.CharField(max_length=128, db_column='DocumentName') # Field name made lowercase.
    receptiondate = models.CharField(max_length=16, db_column='ReceptionDate') # Field name made lowercase.
    fileurl = models.CharField(max_length=255, db_column='FileURL') # Field name made lowercase.
    sendfilestatus = models.SmallIntegerField(db_column='SendFileStatus') # Field name made lowercase.
    observations = models.CharField(max_length=1024, db_column='Observations') # Field name made lowercase.
    associateddata = models.CharField(max_length=255, db_column='AssociatedData') # Field name made lowercase.
    class Meta:
        db_table = '1300-OnBoardDocuments'

class 1500Onmobilelogs(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    logtype = models.SmallIntegerField(db_column='LogType') # Field name made lowercase.
    logtext = models.CharField(max_length=1024, db_column='LogText') # Field name made lowercase.
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    loguser = models.CharField(max_length=36, db_column='LogUser') # Field name made lowercase.
    logdate = models.CharField(max_length=16, db_column='LogDate') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=256, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1500-OnMobileLogs'

class 1505Onmobilehorometers(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    assetcode = models.CharField(max_length=32, db_column='AssetCode') # Field name made lowercase.
    measure = models.FloatField(db_column='Measure') # Field name made lowercase.
    measuredate = models.CharField(max_length=16, db_column='MeasureDate') # Field name made lowercase.
    isreference = models.SmallIntegerField(db_column='IsReference') # Field name made lowercase.
    registryuser = models.CharField(max_length=36, db_column='RegistryUser') # Field name made lowercase.
    numberrotate = models.SmallIntegerField(db_column='NumberRotate') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=256, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '1505-OnMobileHorometers'

class 1510Onmobilesoundingtanksmeasures(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    tankuid = models.CharField(max_length=36, db_column='TankUID') # Field name made lowercase.
    registrydate = models.CharField(max_length=16, db_column='RegistryDate') # Field name made lowercase.
    trim = models.FloatField(db_column='Trim') # Field name made lowercase.
    sounding = models.FloatField(db_column='Sounding') # Field name made lowercase.
    volumen = models.FloatField(db_column='Volumen') # Field name made lowercase.
    weight = models.FloatField(db_column='Weight') # Field name made lowercase.
    comments = models.CharField(max_length=256, db_column='Comments') # Field name made lowercase.
    class Meta:
        db_table = '1510-OnMobileSoundingTanksMeasures'

class 1515Onmobileroutineobjects(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    routineclassuid = models.CharField(max_length=36, db_column='RoutineClassUID') # Field name made lowercase.
    iscomplete = models.SmallIntegerField(db_column='IsComplete') # Field name made lowercase.
    percentage = models.IntegerField(db_column='Percentage') # Field name made lowercase.
    creationdate = models.CharField(max_length=16, db_column='CreationDate') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    canceldate = models.CharField(max_length=16, db_column='CancelDate') # Field name made lowercase.
    canceltype = models.SmallIntegerField(db_column='CancelType') # Field name made lowercase.
    routineuser = models.CharField(max_length=36, db_column='RoutineUser') # Field name made lowercase.
    routinetype = models.SmallIntegerField(db_column='RoutineType') # Field name made lowercase.
    class Meta:
        db_table = '1515-OnMobileRoutineObjects'

class 1520Onmobileroutineactivitiesobjects(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    routineuid = models.CharField(max_length=36, db_column='RoutineUID') # Field name made lowercase.
    routineactivityclassuid = models.CharField(max_length=36, db_column='RoutineActivityClassUID') # Field name made lowercase.
    measurevalue = models.CharField(max_length=32, db_column='MeasureValue') # Field name made lowercase.
    creationdate = models.CharField(max_length=1024, db_column='CreationDate') # Field name made lowercase.
    realizationdate = models.CharField(max_length=16, db_column='RealizationDate') # Field name made lowercase.
    canceldate = models.SmallIntegerField(db_column='CancelDate') # Field name made lowercase.
    routineuser = models.CharField(max_length=36, db_column='RoutineUser') # Field name made lowercase.
    comments = models.CharField(max_length=256, db_column='Comments') # Field name made lowercase.
    class Meta:
        db_table = '1520-OnMobileRoutineActivitiesObjects'

class 1525Onmobileworkorders(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    workorderuid = models.CharField(max_length=36, db_column='WorkOrderUID') # Field name made lowercase.
    iscomplete = models.SmallIntegerField(db_column='IsComplete') # Field name made lowercase.
    percentage = models.IntegerField(db_column='Percentage') # Field name made lowercase.
    creationdate = models.CharField(max_length=16, db_column='CreationDate') # Field name made lowercase.
    enddate = models.CharField(max_length=16, db_column='EndDate') # Field name made lowercase.
    canceldate = models.CharField(max_length=16, db_column='CancelDate') # Field name made lowercase.
    canceltype = models.SmallIntegerField(db_column='CancelType') # Field name made lowercase.
    routineuser = models.CharField(max_length=36, db_column='RoutineUser') # Field name made lowercase.
    routinetype = models.SmallIntegerField(db_column='RoutineType') # Field name made lowercase.
    class Meta:
        db_table = '1525-OnMobileWorkOrders'

class 1530Onmobileworkordersactivities(models.Model):
    uid = models.CharField(max_length=36)
    duid = models.CharField(max_length=36)
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    useruid = models.CharField(max_length=36)
    userdate = models.CharField(max_length=16)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    locationid = models.IntegerField()
    locationcode = models.CharField(max_length=128)
    readytosync = models.SmallIntegerField()
    routineuid = models.CharField(max_length=36, db_column='RoutineUID') # Field name made lowercase.
    routineactivityclassuid = models.CharField(max_length=36, db_column='RoutineActivityClassUID') # Field name made lowercase.
    measurevalue = models.CharField(max_length=32, db_column='MeasureValue') # Field name made lowercase.
    creationdate = models.CharField(max_length=1024, db_column='CreationDate') # Field name made lowercase.
    realizationdate = models.CharField(max_length=16, db_column='RealizationDate') # Field name made lowercase.
    canceldate = models.SmallIntegerField(db_column='CancelDate') # Field name made lowercase.
    routineuser = models.CharField(max_length=36, db_column='RoutineUser') # Field name made lowercase.
    comments = models.CharField(max_length=256, db_column='Comments') # Field name made lowercase.
    class Meta:
        db_table = '1530-OnMobileWorkOrdersActivities'

class 2150Daqonboardgps(models.Model):
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    timestring = models.CharField(max_length=14, db_column='TimeString') # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude') # Field name made lowercase.
    latitudens = models.CharField(max_length=1, db_column='LatitudeNS') # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude') # Field name made lowercase.
    longitudeew = models.CharField(max_length=1, db_column='LongitudeEW') # Field name made lowercase.
    speed = models.FloatField(db_column='Speed') # Field name made lowercase.
    bearing = models.FloatField(db_column='Bearing') # Field name made lowercase.
    pdop = models.FloatField(db_column='Pdop') # Field name made lowercase.
    hdop = models.FloatField(db_column='Hdop') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=128, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '2150-DAQOnBoardGps'

class 2160Daqonboarddata(models.Model):
    regdate = models.CharField(max_length=16)
    regsession = models.CharField(max_length=36)
    vesselid = models.IntegerField()
    vesselname = models.CharField(max_length=64)
    timestring = models.CharField(max_length=14, db_column='TimeString') # Field name made lowercase.
    datacode = models.CharField(max_length=10, db_column='DataCode') # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=128, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '2160-DAQOnBoardData'

class 3000Etltimelapse(models.Model):
    uid = models.TextField()
    timestring = models.CharField(max_length=16, db_column='TimeString') # Field name made lowercase.
    timeyear = models.IntegerField(db_column='TimeYear') # Field name made lowercase.
    timemonth = models.IntegerField(db_column='TimeMonth') # Field name made lowercase.
    timeday = models.IntegerField(db_column='TimeDay') # Field name made lowercase.
    timehour = models.IntegerField(db_column='TimeHour') # Field name made lowercase.
    timeminute = models.IntegerField(db_column='TimeMinute') # Field name made lowercase.
    class Meta:
        db_table = '3000-ETLTimeLapse'

class 3010Etltimeperiods(models.Model):
    uid = models.TextField()
    periodname = models.CharField(max_length=16, db_column='PeriodName') # Field name made lowercase.
    periodtype = models.SmallIntegerField(db_column='PeriodType') # Field name made lowercase.
    inittimeid = models.IntegerField(db_column='InitTimeId') # Field name made lowercase.
    endtimeid = models.IntegerField(db_column='EndTimeId') # Field name made lowercase.
    inittimevalue = models.CharField(max_length=16, db_column='InitTimeValue') # Field name made lowercase.
    endtimevalue = models.CharField(max_length=16, db_column='EndTimeValue') # Field name made lowercase.
    class Meta:
        db_table = '3010-ETLTimePeriods'

class 3020Etlvesselsequipments(models.Model):
    vesseluid = models.CharField(max_length=36, db_column='VesselUid') # Field name made lowercase.
    equipmentname = models.CharField(max_length=32, db_column='EquipmentName') # Field name made lowercase.
    additionaldata = models.CharField(max_length=128, db_column='AdditionalData') # Field name made lowercase.
    class Meta:
        db_table = '3020-ETLVesselsEquipments'

class 3030Etlmeasures(models.Model):
    measuretype = models.SmallIntegerField(db_column='MeasureType') # Field name made lowercase.
    measurecode = models.CharField(max_length=8, db_column='MeasureCode') # Field name made lowercase.
    measurename = models.CharField(max_length=32, db_column='MeasureName') # Field name made lowercase.
    frecuency = models.CharField(max_length=1, db_column='Frecuency') # Field name made lowercase.
    state = models.BooleanField(db_column='State') # Field name made lowercase.
    relateddata = models.CharField(max_length=64, db_column='RelatedData') # Field name made lowercase.
    additionaldata = models.CharField(max_length=128, db_column='AdditionalData') # Field name made lowercase.
    class Meta:
        db_table = '3030-ETLMeasures'

class 3050Etlstaticbasemeasures(models.Model):
    timeid = models.IntegerField(db_column='TimeId') # Field name made lowercase.
    periodid = models.IntegerField(db_column='PeriodId') # Field name made lowercase.
    vesseluid = models.CharField(max_length=36, db_column='VesselUid') # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId') # Field name made lowercase.
    scenarioid = models.SmallIntegerField(db_column='ScenarioId') # Field name made lowercase.
    measureid = models.IntegerField(db_column='MeasureId') # Field name made lowercase.
    measurevalue = models.CharField(max_length=64, db_column='MeasureValue') # Field name made lowercase.
    measuredata = models.CharField(max_length=256, db_column='MeasureData') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    class Meta:
        db_table = '3050-ETLStaticBaseMeasures'

class 3100Etlvesselsopstate(models.Model):
    vesseluid = models.CharField(max_length=36, db_column='VesselUid') # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId') # Field name made lowercase.
    timeid = models.IntegerField(db_column='TimeId') # Field name made lowercase.
    statustype = models.SmallIntegerField(db_column='StatusType') # Field name made lowercase.
    statusvalue = models.FloatField(db_column='StatusValue') # Field name made lowercase.
    class Meta:
        db_table = '3100-ETLVesselsOpState'

class 3110Etlvesselsbudget01(models.Model):
    vesseluid = models.CharField(max_length=36, db_column='VesselUid') # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId') # Field name made lowercase.
    scenarioid = models.SmallIntegerField(db_column='ScenarioId') # Field name made lowercase.
    timeid = models.IntegerField(db_column='TimeId') # Field name made lowercase.
    periodid = models.IntegerField(db_column='PeriodId') # Field name made lowercase.
    dataclass = models.SmallIntegerField(db_column='DataClass') # Field name made lowercase.
    datavalue = models.FloatField(db_column='DataValue') # Field name made lowercase.
    class Meta:
        db_table = '3110-ETLVesselsBudget01'

class 3120Etlequipmentsmeasures(models.Model):
    timeid = models.IntegerField(db_column='TimeId') # Field name made lowercase.
    periodid = models.IntegerField(db_column='PeriodId') # Field name made lowercase.
    vesselid = models.IntegerField(db_column='VesselId') # Field name made lowercase.
    equipmentid = models.IntegerField(db_column='EquipmentId') # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId') # Field name made lowercase.
    scenarioid = models.SmallIntegerField(db_column='ScenarioId') # Field name made lowercase.
    measureid = models.IntegerField(db_column='MeasureId') # Field name made lowercase.
    measurevalue = models.FloatField(db_column='MeasureValue') # Field name made lowercase.
    class Meta:
        db_table = '3120-ETLEquipmentsMeasures'

class 3125Etlgeneral(models.Model):
    timeid = models.IntegerField(db_column='TimeId') # Field name made lowercase.
    periodid = models.IntegerField(db_column='PeriodId') # Field name made lowercase.
    vesseluid = models.CharField(max_length=36, db_column='VesselUid') # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationId') # Field name made lowercase.
    scenarioid = models.SmallIntegerField(db_column='ScenarioId') # Field name made lowercase.
    measureid = models.IntegerField(db_column='MeasureId') # Field name made lowercase.
    measurevalue = models.CharField(max_length=64, db_column='MeasureValue') # Field name made lowercase.
    measuredata = models.CharField(max_length=256, db_column='MeasureData') # Field name made lowercase.
    class Meta:
        db_table = '3125-ETLGeneral'

class 8000Gpstracking(models.Model):
    id = models.AutoField()
    class Meta:
        db_table = '8000-GPSTracking'

class 8020Voicetracking(models.Model):
    id = models.AutoField()
    class Meta:
        db_table = '8020-VoiceTracking'

class 9950Countries(models.Model):
    countryname = models.CharField(max_length=64, db_column='CountryName') # Field name made lowercase.
    countrycode = models.CharField(max_length=2, db_column='CountryCode') # Field name made lowercase.
    continentid = models.SmallIntegerField(db_column='ContinentId') # Field name made lowercase.
    continentname = models.CharField(max_length=36, db_column='ContinentName') # Field name made lowercase.
    status = models.SmallIntegerField(db_column='Status') # Field name made lowercase.
    additionalinfo = models.CharField(max_length=256, db_column='AdditionalInfo') # Field name made lowercase.
    class Meta:
        db_table = '9950-Countries'

class 9952Impaclasses(models.Model):
    title = models.CharField(max_length=128, db_column='Title') # Field name made lowercase.
    titlelang = models.CharField(max_length=2, db_column='TitleLang') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '9952-IMPAClasses'

class 9957Ships(models.Model):
    id = models.AutoField()
    class Meta:
        db_table = '9957-Ships'

class 9980Units(models.Model):
    description = models.CharField(max_length=30, db_column='Description') # Field name made lowercase.
    desclang = models.CharField(max_length=2, db_column='DescLang') # Field name made lowercase.
    system = models.CharField(max_length=3, db_column='System') # Field name made lowercase.
    additionalcode1 = models.CharField(max_length=16, db_column='AdditionalCode1') # Field name made lowercase.
    active = models.SmallIntegerField(db_column='Active') # Field name made lowercase.
    recordversion = models.CharField(max_length=14, db_column='RecordVersion') # Field name made lowercase.
    class Meta:
        db_table = '9980-Units'

class Analysetestsiowebservice(models.Model):
    rownumber = models.IntegerField(primary_key=True, db_column='RowNumber') # Field name made lowercase.
    eventclass = models.IntegerField(null=True, db_column='EventClass', blank=True) # Field name made lowercase.
    textdata = models.TextField(db_column='TextData', blank=True) # Field name made lowercase.
    applicationname = models.CharField(max_length=128, db_column='ApplicationName', blank=True) # Field name made lowercase.
    ntusername = models.CharField(max_length=128, db_column='NTUserName', blank=True) # Field name made lowercase.
    loginname = models.CharField(max_length=128, db_column='LoginName', blank=True) # Field name made lowercase.
    cpu = models.IntegerField(null=True, db_column='CPU', blank=True) # Field name made lowercase.
    reads = models.IntegerField(null=True, db_column='Reads', blank=True) # Field name made lowercase.
    writes = models.IntegerField(null=True, db_column='Writes', blank=True) # Field name made lowercase.
    duration = models.IntegerField(null=True, db_column='Duration', blank=True) # Field name made lowercase.
    clientprocessid = models.IntegerField(null=True, db_column='ClientProcessID', blank=True) # Field name made lowercase.
    spid = models.IntegerField(null=True, db_column='SPID', blank=True) # Field name made lowercase.
    starttime = models.DateTimeField(null=True, db_column='StartTime', blank=True) # Field name made lowercase.
    endtime = models.DateTimeField(null=True, db_column='EndTime', blank=True) # Field name made lowercase.
    binarydata = models.TextField(db_column='BinaryData', blank=True) # Field name made lowercase. This field type is a guess.
    class Meta:
        db_table = 'AnalyseTestSioWebService'

class PFleetstatus(models.Model):
    country = models.CharField(max_length=255, db_column='COUNTRY', blank=True) # Field name made lowercase.
    tug = models.CharField(max_length=255, db_column='TUG', blank=True) # Field name made lowercase.
    supply_chain = models.FloatField(null=True, db_column='SUPPLY_CHAIN', blank=True) # Field name made lowercase.
    center_cost = models.FloatField(null=True, db_column='CENTER_COST', blank=True) # Field name made lowercase.
    shipyard = models.CharField(max_length=255, db_column='SHIPYARD', blank=True) # Field name made lowercase.
    year_of_built = models.FloatField(null=True, db_column='YEAR_OF_BUILT', blank=True) # Field name made lowercase.
    model = models.CharField(max_length=255, db_column='MODEL', blank=True) # Field name made lowercase.
    type = models.CharField(max_length=255, db_column='TYPE', blank=True) # Field name made lowercase.
    engines_bbr = models.CharField(max_length=255, db_column='ENGINES_BBR', blank=True) # Field name made lowercase.
    engines_stb = models.CharField(max_length=255, db_column='ENGINES_STB', blank=True) # Field name made lowercase.
    hp = models.FloatField(null=True, db_column='HP', blank=True) # Field name made lowercase.
    rpm = models.FloatField(null=True, db_column='RPM', blank=True) # Field name made lowercase.
    factory = models.CharField(max_length=255, db_column='FACTORY', blank=True) # Field name made lowercase.
    bollard_pull = models.FloatField(null=True, db_column='BOLLARD_PULL', blank=True) # Field name made lowercase.
    av_2008 = models.FloatField(null=True, db_column='AV_2008', blank=True) # Field name made lowercase.
    av_2009 = models.FloatField(null=True, db_column='AV_2009', blank=True) # Field name made lowercase.
    av_2010 = models.FloatField(null=True, db_column='AV_2010', blank=True) # Field name made lowercase.
    av_2011 = models.FloatField(null=True, db_column='AV_2011', blank=True) # Field name made lowercase.
    re_2008 = models.FloatField(null=True, db_column='RE_2008', blank=True) # Field name made lowercase.
    re_2009 = models.FloatField(null=True, db_column='RE_2009', blank=True) # Field name made lowercase.
    re_2010 = models.FloatField(null=True, db_column='RE_2010', blank=True) # Field name made lowercase.
    re_2011 = models.FloatField(null=True, db_column='RE_2011', blank=True) # Field name made lowercase.
    mtbf_2008 = models.CharField(max_length=255, db_column='MTBF_2008', blank=True) # Field name made lowercase.
    mtbf_2009 = models.CharField(max_length=255, db_column='MTBF_2009', blank=True) # Field name made lowercase.
    mtbf_2010 = models.CharField(max_length=255, db_column='MTBF_2010', blank=True) # Field name made lowercase.
    mtbf_2011 = models.CharField(max_length=255, db_column='MTBF_2011', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'P_FleetStatus'

class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, unique=True)
    principal_id = models.IntegerField(unique=True)
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(null=True, blank=True)
    definition = models.TextField(blank=True) # This field type is a guess.
    class Meta:
        db_table = 'sysdiagrams'

