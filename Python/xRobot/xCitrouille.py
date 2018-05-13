# -*- coding: cp1252 -*-

from Plasma import *
import math
import xClonage

# Objet auquel on va attacher les clones de bille
# (tu peux en choisir un autre)
#so = PtFindSceneobject("MarblePhy01", "Neighborhood")
so = None

##Positions pour la citrouille
#tuplePositions = (
#    ((1.0,0.0,0.0,0.373902879655),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,223.091119385),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.674436984956),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,223.492007446),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.974938093126),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,223.492007446),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.37566574663),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,223.191470337),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.874768148363),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,223.191470337),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.774588190019),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.790765381),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.474021326005),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.490124512),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.17299259752),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.590359497),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.551841320097),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.890878296),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-1.45344230086),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.289605713),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-1.85493747145),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.488209534),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-1.95513183028),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.583154297),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-1.55432130247),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.681599426),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.642824186385),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.280909729),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.0582426652312),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,218.98037262),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.95973623842),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.180717468),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.5608393535),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.08057251),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.86137398332),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.280970764),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,2.56255291551),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.280970764),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,3.15220173448),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.158018494),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,3.2482272014),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.049575806),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,2.94762753099),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.018005371),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,2.05281914324),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.715841675),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.15122402757),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.61545105),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.893757261336),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.415103149),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-1.50221005827),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.514593506),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-1.70293017775),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.512762451),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-1.60288497359),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.911712646),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,2.11515377611),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.313989258),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.60765102953),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.215512085),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.210398103297),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.215512085),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.490663896501),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,222.197763062),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.490663896501),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.569949341),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.362733329833),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.86710968),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.66306964308),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.058226013),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.262297476828),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.058226013),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.138357745111),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.058226013),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.262315310538),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.358779907),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.14672487825),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.859573364),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.846207986772),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.057881165),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.24688452333),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.057881165),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.64753559679),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.057881165),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.24716824144),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,221.358415222),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.481818471849),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.857489014),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.481818471849),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.35296936),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.228758464754),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.35296936),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.781753908098),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.35296936),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,2.1841521129),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.35296936),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.988794054091),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.35296936),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.38418866545),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.152630615),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.428628622),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.152630615),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.827965818346),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.052449036),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.320234809816),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,220.052449036),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.320234809816),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.651416016),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.821040044725),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.651416016),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.02140606493),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.651416016),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.32190817446),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.651416016),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.0602721437812),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.651416016),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.243614973128),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.651416016),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.844239343703),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.851763916),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.90179051012),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.851763916),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.29884003252),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.451029968),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,-0.230263127387),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.451029968),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.0702359065414),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.450891113),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,1.07289522737),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.450891113),(0.0,0.0,0.0,1.0)), 
#    ((1.0,0.0,0.0,0.664033971727),(0.0,1.0,0.0,-275.0),(0.0,0.0,1.0,219.350727844),(0.0,0.0,0.0,1.0)), 
#    )
tuplePositions = (
    ((1,0,0,0.3739028797),(0,1,0,-275),(0,0,1,223.091119385),(0,0,0,1)),
    ((1,0,0,3.3792439327),(0,1,0,-275),(0,0,1,227.099999995),(0,0,0,1)),
    ((1,0,0,6.3842550144),(0,1,0,-275),(0,0,1,227.099999995),(0,0,0,1)),
    ((1,0,0,10.3915315494),(0,1,0,-275),(0,0,1,224.094628905),(0,0,0,1)),
    ((1,0,0,5.3825555667),(0,1,0,-275),(0,0,1,224.094628905),(0,0,0,1)),
    ((1,0,0,4.3807559833),(0,1,0,-275),(0,0,1,220.087579345),(0,0,0,1)),
    ((1,0,0,1.3750873432),(0,1,0,-275),(0,0,1,217.081170655),(0,0,0,1)),
    ((1,0,0,-1.6351999417),(0,1,0,-275),(0,0,1,218.083520505),(0,0,0,1)),
    ((1,0,0,-8.8835391179),(0,1,0,-275),(0,0,1,221.088708495),(0,0,0,1)),
    ((1,0,0,-17.8995489255),(0,1,0,-275),(0,0,1,215.075982665),(0,0,0,1)),
    ((1,0,0,-21.9145006314),(0,1,0,-275),(0,0,1,207.062020875),(0,0,0,1)),
    ((1,0,0,-22.9164442197),(0,1,0,-275),(0,0,1,198.011468505),(0,0,0,1)),
    ((1,0,0,-18.9083389416),(0,1,0,-275),(0,0,1,188.995919795),(0,0,0,1)),
    ((1,0,0,-9.7933677807),(0,1,0,-275),(0,0,1,184.989022825),(0,0,0,1)),
    ((1,0,0,-2.7826992646),(0,1,0,-275),(0,0,1,181.983651735),(0,0,0,1)),
    ((1,0,0,6.2322364673),(0,1,0,-275),(0,0,1,183.987100215),(0,0,0,1)),
    ((1,0,0,12.2432676181),(0,1,0,-275),(0,0,1,182.985650635),(0,0,0,1)),
    ((1,0,0,15.2486139163),(0,1,0,-275),(0,0,1,184.989633175),(0,0,0,1)),
    ((1,0,0,22.2604032382),(0,1,0,-275),(0,0,1,184.989633175),(0,0,0,1)),
    ((1,0,0,28.1568914279),(0,1,0,-275),(0,0,1,193.760110475),(0,0,0,1)),
    ((1,0,0,29.1171460971),(0,1,0,-275),(0,0,1,202.675683595),(0,0,0,1)),
    ((1,0,0,26.111149393),(0,1,0,-275),(0,0,1,212.359979245),(0,0,0,1)),
    ((1,0,0,17.1630655155),(0,1,0,-275),(0,0,1,219.338342285),(0,0,0,1)),
    ((1,0,0,8.1471143588),(0,1,0,-275),(0,0,1,218.334436035),(0,0,0,1)),
    ((1,0,0,-12.3026985303),(0,1,0,-275),(0,0,1,216.330957025),(0,0,0,1)),
    ((1,0,0,-18.3872264996),(0,1,0,-275),(0,0,1,207.325860595),(0,0,0,1)),
    ((1,0,0,-20.3944276944),(0,1,0,-275),(0,0,1,197.307550045),(0,0,0,1)),
    ((1,0,0,-19.3939756528),(0,1,0,-275),(0,0,1,191.297051995),(0,0,0,1)),
    ((1,0,0,17.7864118442),(0,1,0,-275),(0,0,1,205.319818115),(0,0,0,1)),
    ((1,0,0,12.7113843784),(0,1,0,-275),(0,0,1,214.335046385),(0,0,0,1)),
    ((1,0,0,-5.4691069499),(0,1,0,-275),(0,0,1,214.335046385),(0,0,0,1)),
    ((1,0,0,1.5415130481),(0,1,0,-275),(0,0,1,214.157556155),(0,0,0,1)),
    ((1,0,0,1.5415130481),(0,1,0,-275),(0,0,1,207.879418945),(0,0,0,1)),
    ((1,0,0,-6.9924592152),(0,1,0,-275),(0,0,1,210.851022335),(0,0,0,1)),
    ((1,0,0,-9.9958223477),(0,1,0,-275),(0,0,1,202.762185665),(0,0,0,1)),
    ((1,0,0,-5.9881006852),(0,1,0,-275),(0,0,1,202.762185665),(0,0,0,1)),
    ((1,0,0,-1.9815484658),(0,1,0,-275),(0,0,1,202.762185665),(0,0,0,1)),
    ((1,0,0,-5.9882790223),(0,1,0,-275),(0,0,1,205.767724605),(0,0,0,1)),
    ((1,0,0,8.1021228656),(0,1,0,-275),(0,0,1,210.775659175),(0,0,0,1)),
    ((1,0,0,5.0969539508),(0,1,0,-275),(0,0,1,202.758737185),(0,0,0,1)),
    ((1,0,0,9.1037193164),(0,1,0,-275),(0,0,1,202.758737185),(0,0,0,1)),
    ((1,0,0,13.110230051),(0,1,0,-275),(0,0,1,202.758737185),(0,0,0,1)),
    ((1,0,0,9.1065564975),(0,1,0,-275),(0,0,1,205.764077755),(0,0,0,1)),
    ((1,0,0,1.4530588016),(0,1,0,-275),(0,0,1,200.754815675),(0,0,0,1)),
    ((1,0,0,1.4530588016),(0,1,0,-275),(0,0,1,195.709619135),(0,0,0,1)),
    ((1,0,0,-1.0775412694),(0,1,0,-275),(0,0,1,195.709619135),(0,0,0,1)),
    ((1,0,0,4.4524131641),(0,1,0,-275),(0,0,1,195.709619135),(0,0,0,1)),
    ((1,0,0,18.4763952121),(0,1,0,-275),(0,0,1,195.709619135),(0,0,0,1)),
    ((1,0,0,-13.2530664578),(0,1,0,-275),(0,0,1,195.709619135),(0,0,0,1)),
    ((1,0,0,-7.2070125714),(0,1,0,-275),(0,0,1,193.706231685),(0,0,0,1)),
    ((1,0,0,10.9211603031),(0,1,0,-275),(0,0,1,193.706231685),(0,0,0,1)),
    ((1,0,0,4.9145322666),(0,1,0,-275),(0,0,1,192.704415895),(0,0,0,1)),
    ((1,0,0,-0.1627778187),(0,1,0,-275),(0,0,1,192.704415895),(0,0,0,1)),
    ((1,0,0,-0.1627778187),(0,1,0,-275),(0,0,1,188.694085695),(0,0,0,1)),
    ((1,0,0,4.8452745304),(0,1,0,-275),(0,0,1,188.694085695),(0,0,0,1)),
    ((1,0,0,6.8489347324),(0,1,0,-275),(0,0,1,188.694085695),(0,0,0,1)),
    ((1,0,0,9.8539558277),(0,1,0,-275),(0,0,1,188.694085695),(0,0,0,1)),
    ((1,0,0,-2.7624044791),(0,1,0,-275),(0,0,1,188.694085695),(0,0,0,1)),
    ((1,0,0,-5.8012756482),(0,1,0,-275),(0,0,1,188.694085695),(0,0,0,1)),
    ((1,0,0,-11.8075193539),(0,1,0,-275),(0,0,1,190.697564695),(0,0,0,1)),
    ((1,0,0,15.6527791843),(0,1,0,-275),(0,0,1,190.697564695),(0,0,0,1)),
    ((1,0,0,9.6232744083),(0,1,0,-275),(0,0,1,186.690225215),(0,0,0,1)),
    ((1,0,0,-5.6677571908),(0,1,0,-275),(0,0,1,186.690225215),(0,0,0,1)),
    ((1,0,0,-2.6627668515),(0,1,0,-275),(0,0,1,186.688836665),(0,0,0,1)),
    ((1,0,0,7.3638263568),(0,1,0,-275),(0,0,1,186.688836665),(0,0,0,1)),
    ((1,0,0,3.2752138004),(0,1,0,-275),(0,0,1,185.687203975),(0,0,0,1)),
    )
# Initialise 
def Init():
    global so
    PtSetAlarm(0, AlarmInit(), 1)

#
class AlarmInit():
    def __init__(self):
        self._nbFois = 0
        self._so = None
        #Charger nb01: pas indispensable
        #PtConsoleNet("Nav.PageInNode %s" % ("nb01") , 1)
        
    def onAlarm(self, param):
        if param == 1:
            print "AlarmInit onAlarm 1"
            #self._so = PtFindSceneobject("MarblePhy01", "Neighborhood")
            self._so = PtFindSceneobject("GPSGreatZero", "Neighborhood")
            # Attendre que self._so soit charge
            if (self._so is None and self._nbFois < 20):
                self._nbFois += 1
                print ">>> Attente nb: %i" % self._nbFois
                PtSetAlarm(1, self, 1)
            else:
                PtSetAlarm(1, self, 2)
        elif param == 2:
            print "AlarmInit onAlarm 2"
            #initialiser les dictionnaires de clonage
            xClonage.InitDicts()
            #
            if self._so != None:
                global so
                so = self._so
                self._so.netForce(1)
                self._so.physics.enable(0)
                nb = len(tuplePositions)
                AfficherElement(-8, 7, "red", nb, self._so)
                #PtSetAlarm (1, AlarmAffichage(0, 7, "yellow", nb, self._so), 1)
                #PtSetAlarm (1, AlarmAffichage(0, 7, "white", nb, self._so), 1)
                #PtSetAlarm (1, AlarmAffichage(8, 7, "blue", nb, self._so), 1)
            else:
                pass
        else:
            print "AlarmInit onAlarm mauvais param"

#Permet de creer un element de clones de FireMarbles
def AfficherElement(dist, hauteur, couleur = None, nb = None, av = None):
    xClonage.dicClonesPhy
    #av peut etre n'importe quel scene object ayant des coordonnees
    if av == None:
        av = PtGetLocalAvatar()
    if couleur == None:
        couleur = "yellow"
    if nb == None:
        # taille de tuplePositions
        nb = len(tuplePositions)
    # combien de clones a-t-on deja a disposition?
    nbClones = len(xClonage.dicClonesPhy[couleur])
    print "nb de clones %s %i" % (couleur, nbClones)

    #Ajouter des clones si besoin
    if nbClones < nb:
        xClonage.Cloner(nb - nbClones)
    print "> AfficherElement : appel a Dessiner..."
    PtSetAlarm(1, Dessiner(av, nb, couleur, dist, hauteur), 1)
    print "> AfficherElement : FIN"


# Dessine-moi une citrouille...
class Dessiner():
    xClonage.dicClonesPhy
    xClonage.dicClonesDra
    
    _so = None
    _nbClones = 0
    _couleur = "yellow"
    _dist = 3
    _hauteur = 4
    _nbFois = 0
    
    def __init__(self, so, nbClones, couleur, dist, hauteur):
        print "> Dessiner : INIT"
        self._so = so
        self._nbClones = nbClones
        self._couleur = couleur
        self._dist = dist
        self._hauteur = hauteur
        print "> Dessiner : INIT ok"
    
    def onAlarm(self, param):
        print "> Dessiner : onAlarm"
        if param == 1:
            nbClonesFound = len(xClonage.dicClonesPhy[self._couleur])
            print "> Dessiner : nb de clones %s %i" % (self._couleur, nbClonesFound)
            # Attendre que tous les clones soient crees, mais pas indefiniment
            if (nbClonesFound < self._nbClones and self._nbFois < 20):
                self._nbFois += 1
                print ">>> Attente nb: %i" % self._nbFois
                PtSetAlarm(1, self, 1)
            else:
                PtSetAlarm(1, self, 2)
        elif param == 2:
            print "> Dessiner : nb de clones %s %i" % (self._couleur, self._nbClones)
            ## J'ai fixe l'espacement a 2, peut etre mis en parametre
            #element = CreerElement(2)
            
            for i in range(len(tuplePositions)):
                print "> Dessiner : i = {}".format(i)
                sop = xClonage.dicClonesPhy[self._couleur][i].getSceneObject()
                sod = xClonage.dicClonesDra[self._couleur][i].getSceneObject()
                #dx = tuplePositions[i][0][3] + self._dist
                #dy = tuplePositions[i][1][3]
                #dz = self._hauteur + 8 - element[i][2][3]
                sop.physics.netForce(1)
                sod.draw.netForce(1)
                #xClonage.Attacher(sop, self._so, dx, dy, dz, False)
                #xClonage.Deplacer(sop, self._so, dx, dy, dz, False)
                matPos = ptMatrix44()
                matPos.setData(tuplePositions[i])
                sop.physics.warp(matPos)
                sop.physics.disable()
        else:
            pass
        print "> Dessiner : FIN"

#
