from Plasma import *

def load():
    PtConsoleNet('Nav.PageInNode desert', 1)
    PtSetAlarm(1,dis(),0)
    PtSetAlarm(1,hide(),0)
    #PtSetAlarm(1,morehide(),0)
    print 'The floor is completely safe :)';
    
class dis:
    def onAlarm(self,context): 
        age = '' #'desert'
        objectName = 'ProxyPropertyLine'
        obj = PtFindSceneobject(objectName, '') #age)
        obj1 = PtFindSceneobject('PlayerBlockerTemp', '')
        obj2 = PtFindSceneobject('DesertRockSmall05', '')
        obj3 = PtFindSceneobject('DesertRockSmall06', '')
        obj4 = PtFindSceneobject('DesertRockSmall07', '')
        obj5 = PtFindSceneobject('DesertRockSmall08', '')
        obj6 = PtFindSceneobject('DesertRockSmall09', '')
        obj7 = PtFindSceneobject('DesertRockSmall10', '')
        obj8 = PtFindSceneobject('DesertRockSmall11', '')
        obj9 = PtFindSceneobject('DesertRockSmall12', '')
        obj10 = PtFindSceneobject('DesertRockSmall13', '')
        obj11 = PtFindSceneobject('DesertRockSmall14', '')
        obj12 = PtFindSceneobject('DesertRockSmall15', '')
        obj13 = PtFindSceneobject('DesertRockSmall16', '')
        obj14 = PtFindSceneobject('DesertRockSmall17', '')
        obj15 = PtFindSceneobject('DesertRockSmall18', '')
        obj16 = PtFindSceneobject('DesertRockSmall19', '')
        obj17 = PtFindSceneobject('DesertRockSmall20', '')
        obj18 = PtFindSceneobject('DesertRockSmall21', '')
        obj19 = PtFindSceneobject('DesertRockSmall22', '')
        obj20 = PtFindSceneobject('PostProxy', '')
        obj21 = PtFindSceneobject('PostProxy02', '')
        obj22 = PtFindSceneobject('RockProxy01', '')
        obj23 = PtFindSceneobject('RockProxy02', '')
        obj24 = PtFindSceneobject('RockProxy03', '')
        obj25 = PtFindSceneobject('RockProxy04', '')
        obj26 = PtFindSceneobject('LinkInPointDefault', '')
        #obj27 = PtFindSceneobject('DCSoarBird01', '')
        #obj28 = PtFindSceneobject('DCSoarBird03', '')
        obj29 = PtFindSceneobject('CD', '')
        obj30 = PtFindSceneobject('Box01', '')
        obj31 = PtFindSceneobject('Box02', '')
        obj32 = PtFindSceneobject('Box06', '')
        obj33 = PtFindSceneobject('Box07', '')
        obj34 = PtFindSceneobject('PropertySign', '')
        obj35 = PtFindSceneobject('Zandi CAm Blocker', '')
        obj36 = PtFindSceneobject('ZandiCam', '')
        obj37 = PtFindSceneobject('ZandiCam.target', '')
        obj38 = PtFindSceneobject('ZandiCamRegionSafe', '')
        obj39 = PtFindSceneobject('SfxRegSen-Music-Start01', '')
        #obj40 = PtFindSceneobject('SfxRegSen-Music-Stop01', '')
        obj41 = PtFindSceneobject('SfxRegSenMusic-Start02', '')
        obj42 = PtFindSceneobject('SfxRegSenMusic-Start03', '')
        obj43 = PtFindSceneobject('SfxRegSenFeet-Dirt01', '')
        obj.physics.netForce(1)
        obj.physics.enable(0)
        obj1.physics.netForce(1)
        obj1.physics.enable(0)
        obj2.physics.netForce(1)
        obj2.physics.enable(0)
        obj3.physics.netForce(1)
        obj3.physics.enable(0)
        obj4.physics.netForce(1)
        obj4.physics.enable(0)
        obj5.physics.netForce(1)
        obj5.physics.enable(0)
        obj6.physics.netForce(1)
        obj6.physics.enable(0)
        obj7.physics.netForce(1)
        obj7.physics.enable(0)
        obj8.physics.netForce(1)
        obj8.physics.enable(0)
        obj9.physics.netForce(1)
        obj9.physics.enable(0)
        obj10.physics.netForce(1)
        obj10.physics.enable(0)
        obj11.physics.netForce(1)
        obj11.physics.enable(0)
        obj12.physics.netForce(1)
        obj12.physics.enable(0)
        obj13.physics.netForce(1)
        obj13.physics.enable(0)
        obj14.physics.netForce(1)
        obj14.physics.enable(0)
        obj15.physics.netForce(1)
        obj15.physics.enable(0)
        obj16.physics.netForce(1)
        obj16.physics.enable(0)
        obj17.physics.netForce(1)
        obj17.physics.enable(0)
        obj18.physics.netForce(1)
        obj18.physics.enable(0)
        obj19.physics.netForce(1)
        obj19.physics.enable(0)
        obj20.physics.netForce(1)
        obj20.physics.enable(0)
        obj21.physics.netForce(1)
        obj21.physics.enable(0)
        obj22.physics.netForce(1)
        obj22.physics.enable(0)
        obj23.physics.netForce(1)
        obj23.physics.enable(0)
        obj24.physics.netForce(1)
        obj24.physics.enable(0)
        obj25.physics.netForce(1)
        obj25.physics.enable(0)
        obj26.physics.netForce(1)
        obj26.physics.enable(0)
        #obj27.physics.netForce(1)
        #obj27.physics.enable(0)
        #obj28.physics.netForce(1)
        #obj28.physics.enable(0)
        obj29.physics.netForce(1)
        obj29.physics.enable(0)
        obj30.physics.netForce(1)
        obj30.physics.enable(0)
        obj31.physics.netForce(1)
        obj31.physics.enable(0)
        obj32.physics.netForce(1)
        obj32.physics.enable(0)
        obj33.physics.netForce(1)
        obj33.physics.enable(0)
        obj34.physics.netForce(1)
        obj34.physics.enable(0)
        obj35.physics.netForce(1)
        obj35.physics.enable(0)
        obj36.physics.netForce(1)
        obj36.physics.enable(0)
        obj37.physics.netForce(1)
        obj37.physics.enable(0)
        obj38.physics.netForce(1)
        obj38.physics.enable(0)
        obj39.physics.netForce(1)
        obj39.physics.enable(0)
        #obj40.physics.netForce(1)
        #obj40.physics.enable(0)
        obj41.physics.netForce(1)
        obj41.physics.enable(0)
        obj42.physics.netForce(1)
        obj42.physics.enable(0)
        obj43.physics.netForce(1)
        obj43.physics.enable(0)
        print 'All undesired objects have been disabled'; 

class hide:
    def onAlarm(self,context): 
        age = '' #'desert'
        objectName = 'WideBarbedWire'
        obj = PtFindSceneobject(objectName, '') #age)
        obj44 = PtFindSceneobject('PlayerBlockerTemp', '')
        obj45 = PtFindSceneobject('MountainRangeSplit', '')
        obj46 = PtFindSceneobject('MountainRangeSplit2', '')
        obj47 = PtFindSceneobject('DistantShrubsStrip01', '')
        obj48 = PtFindSceneobject('DistantShrubsStrip02', '')
        obj49 = PtFindSceneobject('DistantShrubsStrip03', '')
        obj50 = PtFindSceneobject('DistantDryBrushStrip', '')
        obj51 = PtFindSceneobject('DistantDryBrushStrip02', '')
        obj52 = PtFindSceneobject('DistantDryBrushStrip03', '')
        obj53 = PtFindSceneobject('DistantDryBrushStrip04', '')
        obj54 = PtFindSceneobject('DistantShrubDecalx', '')
        obj55 = PtFindSceneobject('DesertPlane', '')
        obj56 = PtFindSceneobject('DesertPlane1', '')
        obj57 = PtFindSceneobject('DesertPlane2', '')
        obj58 = PtFindSceneobject('DesertPlane3', '')
        obj59 = PtFindSceneobject('DesertPlane4', '')
        obj60 = PtFindSceneobject('farOffMountainRange', '')
        obj61 = PtFindSceneobject('SunBlockerLOS', '')
        obj62 = PtFindSceneobject('SunBack', '')
        obj63 = PtFindSceneobject('skyDome', 'Cleft')
        obj64 = PtFindSceneobject('DesertPlanDecal1', '')
        obj65 = PtFindSceneobject('DesertRockSmall05', '')
        obj66 = PtFindSceneobject('DesertRockSmall06', '')
        obj67 = PtFindSceneobject('DesertRockSmall07', '')
        obj68 = PtFindSceneobject('DesertRockSmall08', '')
        obj69 = PtFindSceneobject('DesertRockSmall09', '')
        obj70 = PtFindSceneobject('DesertRockSmall10', '')
        obj71 = PtFindSceneobject('DesertRockSmall11', '')
        obj72 = PtFindSceneobject('DesertRockSmall12', '')
        obj73 = PtFindSceneobject('DesertRockSmall13', '')
        obj74 = PtFindSceneobject('DesertRockSmall14', '')
        obj75 = PtFindSceneobject('DesertRockSmall15', '')
        obj76 = PtFindSceneobject('DesertRockSmall16', '')
        obj77 = PtFindSceneobject('DesertRockSmall17', '')
        obj78 = PtFindSceneobject('DesertRockSmall18', '')
        obj79 = PtFindSceneobject('DesertRockSmall19', '')
        obj80 = PtFindSceneobject('DesertRockSmall20', '')
        obj81 = PtFindSceneobject('DesertRockSmall21', '')
        obj82 = PtFindSceneobject('DesertRockSmall22', '')
        obj83 = PtFindSceneobject('DesertPlainDecal2', '')
        obj84 = PtFindSceneobject('DesertPlainDecal3', '')
        obj85 = PtFindSceneobject('DesertPlainDecal4', '')
        obj86 = PtFindSceneobject('DriftSand', '')
        obj87 = PtFindSceneobject('GateRutDecal', '')
        obj88 = PtFindSceneobject('MoundSign', '')
        obj89 = PtFindSceneobject('NegativeSunlightRegion', '')
        obj90 = PtFindSceneobject('Object01', '')
        obj91 = PtFindSceneobject('Occluder01', '')
        obj92 = PtFindSceneobject('Occluder02', '')
        obj93 = PtFindSceneobject('Plane01', '')
        obj94 = PtFindSceneobject('PostShadDecal', '')
        obj95 = PtFindSceneobject('PropertySign', '')
        obj96 = PtFindSceneobject('ScrubBrush', '')
        obj97 = PtFindSceneobject('ScrubBrushHigh', '')
        obj98 = PtFindSceneobject('ScrubBrushUltra', '')
        obj99 = PtFindSceneobject('SignPost02', '')
        obj100 = PtFindSceneobject('StrawVolcanoShadow', '')
        obj101 = PtFindSceneobject('TheVolcano', '')
        #obj102 = PtFindSceneobject('Torus01', '')
        obj103 = PtFindSceneobject('VolcanoDarkRegion', '')
        obj104 = PtFindSceneobject('VolcanoShad', '')
        obj105 = PtFindSceneobject('WeedsHigh', '')
        obj106 = PtFindSceneobject('WeedsUltra', '')
        obj107 = PtFindSceneobject('WindWallShadDecal', '')
        obj108 = PtFindSceneobject('trailerShadowDecalNew', '')
        obj109 = PtFindSceneobject('PostBarbedTypeA', '')
        obj110 = PtFindSceneobject('PostBarbedTypeA01', '')
        obj111 = PtFindSceneobject('PostBarbedTypeA02', '')
        obj112 = PtFindSceneobject('PostBarbedTypeA03', '')
        obj113 = PtFindSceneobject('PostBarbedTypeA04', '')
        obj114 = PtFindSceneobject('PostBarbedTypeA05', '')
        obj115 = PtFindSceneobject('PostBarbedTypeA06', '')
        obj116 = PtFindSceneobject('PostBarbedTypeA07', '')
        obj117 = PtFindSceneobject('PostBarbedTypeA08', '')
        obj118 = PtFindSceneobject('PostBarbedTypeA09', '')
        obj119 = PtFindSceneobject('PostBarbedTypeA10', '')
        obj120 = PtFindSceneobject('PostBarbedTypeA11', '')
        obj121 = PtFindSceneobject('PostBarbedTypeA12', '')
        obj122 = PtFindSceneobject('PostBarbedTypeA13', '')
        obj123 = PtFindSceneobject('PostBarbedTypeA14', '')
        obj124 = PtFindSceneobject('PostBarbedTypeA15', '')
        obj125 = PtFindSceneobject('PostBarbedTypeA16', '')
        obj126 = PtFindSceneobject('PostBarbedTypeA18', '')
        obj127 = PtFindSceneobject('PostBarbedTypeA20', '')
        obj128 = PtFindSceneobject('PostBarbedTypeA21', '')
        obj129 = PtFindSceneobject('PostBarbedTypeA22', '')
        obj130 = PtFindSceneobject('PostBarbedTypeA23', '')
        obj131 = PtFindSceneobject('PostBarbedTypeA24', '')
        obj132 = PtFindSceneobject('PostBarbedTypeA25', '')
        #obj133 = PtFindSceneobject('PostBarbedTypeA26', '')
        obj134 = PtFindSceneobject('PostBarbedTypeA27', '')
        obj135 = PtFindSceneobject('PostBarbedTypeA28', '')
        obj136 = PtFindSceneobject('PostBarbedTypeA29', '')
        obj137 = PtFindSceneobject('PostBarbedTypeB', '')
        obj138 = PtFindSceneobject('PostBarbedTypeB01', '')
        obj139 = PtFindSceneobject('PostBarbedTypeB02', '')
        obj140 = PtFindSceneobject('PostBarbedTypeB05', '')
        obj141 = PtFindSceneobject('PostBarbedTypeB06', '')
        obj142 = PtFindSceneobject('PostBarbedTypeB11', '')
        obj143 = PtFindSceneobject('PostBarbedTypeB12', '')
        obj144 = PtFindSceneobject('PostBarbedTypeB13', '')
        obj145 = PtFindSceneobject('PostBarbedTypeB14', '')
        obj146 = PtFindSceneobject('PostBarbedTypeB15', '')
        obj147 = PtFindSceneobject('PostBarbedTypeB16', '')
        obj148 = PtFindSceneobject('PostBarbedTypeB17', '')
        obj149 = PtFindSceneobject('PostBarbedTypeB19', '')
        obj150 = PtFindSceneobject('PostBarbedTypeB20', '')
        obj151 = PtFindSceneobject('PostBarbedTypeB21', '')
        obj152 = PtFindSceneobject('PostBarbedTypeB22', '')
        obj153 = PtFindSceneobject('PostBarbedTypeB23', '')
        obj154 = PtFindSceneobject('PostBarbedTypeB24', '')
        obj155 = PtFindSceneobject('PostBarbedTypeB25', '')
        obj156 = PtFindSceneobject('PostBarbedTypeB26', '')
        obj157 = PtFindSceneobject('PostBarbedTypeB27', '')
        obj158 = PtFindSceneobject('PostBarbedTypeB29', '')
        obj159 = PtFindSceneobject('PostBarbedTypeC01', '')
        obj160 = PtFindSceneobject('PostBarbedTypeC02', '')
        obj161 = PtFindSceneobject('PostBarbedTypeC03', '')
        obj162 = PtFindSceneobject('PostBarbedTypeC04', '')
        obj163 = PtFindSceneobject('PostBarbedTypeC07', '')
        obj164 = PtFindSceneobject('PostBarbedTypeC08', '')
        obj165 = PtFindSceneobject('PostBarbedTypeC09', '')
        obj166 = PtFindSceneobject('PostBarbedTypeC10', '')
        obj167 = PtFindSceneobject('PostBarbedTypeC16', '')
        obj168 = PtFindSceneobject('PostBarbedTypeC17', '')
        obj169 = PtFindSceneobject('PostBarbedTypeC18', '')
        obj170 = PtFindSceneobject('PostBarbedTypeC19', '')
        obj171 = PtFindSceneobject('PostBarbedTypeC24', '')
        obj172 = PtFindSceneobject('PostBarbedTypeC25', '')
        obj173 = PtFindSceneobject('PostBarbedTypeC26', '')
        obj174 = PtFindSceneobject('PostBarbedTypeC27', '')
        obj175 = PtFindSceneobject('PostBarbedTypeC28', '')
        obj176 = PtFindSceneobject('PostBarbedTypeC29', '')
        obj177 = PtFindSceneobject('PostBarbedTypeD', '')
        obj178 = PtFindSceneobject('PostBarbedTypeD03', '')
        obj179 = PtFindSceneobject('PostBarbedTypeD04', '')
        obj180 = PtFindSceneobject('PostBarbedTypeD05', '')
        obj181 = PtFindSceneobject('PostBarbedTypeD06', '')
        obj182 = PtFindSceneobject('PostBarbedTypeD07', '')
        obj183 = PtFindSceneobject('PostBarbedTypeD08', '')
        obj184 = PtFindSceneobject('PostBarbedTypeD09', '')
        obj185 = PtFindSceneobject('PostBarbedTypeD10', '')
        obj186 = PtFindSceneobject('PostBarbedTypeD11', '')
        obj187 = PtFindSceneobject('PostBarbedTypeD12', '')
        obj188 = PtFindSceneobject('PostBarbedTypeD13', '')
        obj189 = PtFindSceneobject('PostBarbedTypeD14', '')
        obj190 = PtFindSceneobject('PostBarbedTypeD15', '')
        obj191 = PtFindSceneobject('PostBarbedTypeD16', '')
        obj192 = PtFindSceneobject('PostBarbedTypeD17', '')
        obj193 = PtFindSceneobject('PostBarbedTypeD18', '')
        obj194 = PtFindSceneobject('PostBarbedTypeD20', '')
        obj195 = PtFindSceneobject('PostBarbedTypeD21', '')
        obj196 = PtFindSceneobject('PostBarbedTypeD22', '')
        obj197 = PtFindSceneobject('PostBarbedTypeD23', '')
        obj198 = PtFindSceneobject('PostBarbedTypeD25', '')
        obj199 = PtFindSceneobject('PostBarbedTypeD26', '')
        obj200 = PtFindSceneobject('PostBarbedTypeD27', '')
        obj201 = PtFindSceneobject('PostBarbedTypeD28', '')
        obj202 = PtFindSceneobject('PostBarbedTypeD29', '')
        #obj203 = PtFindSceneobject('DCSoarBird01', '')
        obj204 = PtFindSceneobject('Lash01', '')
        obj205 = PtFindSceneobject('Lash02', '')
        obj206 = PtFindSceneobject('Lash03', '')
        obj207 = PtFindSceneobject('Lash04', '')
        obj208 = PtFindSceneobject('Lash05', '')
        obj209 = PtFindSceneobject('Lash06', '')
        obj210 = PtFindSceneobject('Lash08', '')
        obj211 = PtFindSceneobject('Lash09', '')
        obj212 = PtFindSceneobject('Lash11', '')
        obj213 = PtFindSceneobject('Lash12', '')
        #obj214 = PtFindSceneobject('DCSoarBird03', '')
        obj215 = PtFindSceneobject('CleftLipDecal', '')
        obj216 = PtFindSceneobject('CD', '')
        obj217 = PtFindSceneobject('TelescopeSandDecal01', '')
        obj218 = PtFindSceneobject('TelescopeSandDecal02', '')
        obj219 = PtFindSceneobject('TelescopeSandDecal03', '')
        obj220 = PtFindSceneobject('TrailerRutDecal', '')
        obj221 = PtFindSceneobject('PostProxy02', '')
        obj222 = PtFindSceneobject('radioHandle', '')
        obj223 = PtFindSceneobject('radio', '')
        obj224 = PtFindSceneobject('propaneBBQ02', '')
        obj225 = PtFindSceneobject('cooler', '')
        obj226 = PtFindSceneobject('chipsBag', '')
        obj227 = PtFindSceneobject('burgerPatty', '')
        obj228 = PtFindSceneobject('GrillTop', '')
        obj229 = PtFindSceneobject('Grill03', '')
        obj230 = PtFindSceneobject('Grill', '')
        obj231 = PtFindSceneobject('BeerCan01', '')
        obj232 = PtFindSceneobject('BeerCan02', '')
        obj233 = PtFindSceneobject('awningEdgeRod01', '')
        obj234 = PtFindSceneobject('awningEdgeRod02', '')
        obj235 = PtFindSceneobject('awningHinge01', '')
        obj236 = PtFindSceneobject('awningHinge02', '')
        obj237 = PtFindSceneobject('awningSupport01', '')
        obj238 = PtFindSceneobject('awningSupport02', '')
        obj239 = PtFindSceneobject('awningTopSide', '')
        obj240 = PtFindSceneobject('awningUnderSide', '')
        obj241 = PtFindSceneobject('tableLeg01', '')
        obj242 = PtFindSceneobject('tableLeg02', '')
        obj243 = PtFindSceneobject('tableTop02', '')
        obj244 = PtFindSceneobject('ZandiChair01', '')
        obj245 = PtFindSceneobject('ZandiChair02', '')
        obj246 = PtFindSceneobject('ZandiChair06', '')
        obj247 = PtFindSceneobject('ZandiChair07', '')
        obj248 = PtFindSceneobject('ZandiChair13', '')
        obj249 = PtFindSceneobject('ZandiChair14', '')
        obj250 = PtFindSceneobject('ZandiChair15', '')
        obj251 = PtFindSceneobject('ZandiChair16', '')
        obj252 = PtFindSceneobject('ZandiChair17', '')
        obj253 = PtFindSceneobject('ZandiChair18', '')
        obj254 = PtFindSceneobject('ZandiChair20', '')
        obj255 = PtFindSceneobject('ZandiChair24', '')
        obj256 = PtFindSceneobject('ZandiChair25', '')
        obj257 = PtFindSceneobject('ZandiChair26', '')
        obj258 = PtFindSceneobject('ZandiChair27', '')
        obj259 = PtFindSceneobject('ZandiChair28', '')
        obj.draw.netForce(1)
        obj.draw.enable(0)
        obj44.draw.netForce(1)
        obj44.draw.enable(0)
        obj45.draw.netForce(1)
        obj45.draw.enable(0)
        obj46.draw.netForce(1)
        obj46.draw.enable(0)
        obj47.draw.netForce(1)
        obj47.draw.enable(0)
        obj48.draw.netForce(1)
        obj48.draw.enable(0)
        obj49.draw.netForce(1)
        obj49.draw.enable(0)
        obj50.draw.netForce(1)
        obj50.draw.enable(0)
        obj51.draw.netForce(1)
        obj51.draw.enable(0)
        obj52.draw.netForce(1)
        obj52.draw.enable(0)
        obj53.draw.netForce(1)
        obj53.draw.enable(0)
        obj54.draw.netForce(1)
        obj54.draw.enable(0)
        obj55.draw.netForce(1)
        obj55.draw.enable(0)
        obj56.draw.netForce(1)
        obj56.draw.enable(0)
        obj57.draw.netForce(1)
        obj57.draw.enable(0)
        obj58.draw.netForce(1)
        obj58.draw.enable(0)
        obj59.draw.netForce(1)
        obj59.draw.enable(0)
        obj60.draw.netForce(1)
        obj60.draw.enable(0)
        obj61.draw.netForce(1)
        obj61.draw.enable(0)
        obj62.draw.netForce(1)
        obj62.draw.enable(0)
        obj63.draw.netForce(1)
        obj63.draw.enable(0)
        obj64.draw.netForce(1)
        obj64.draw.enable(0)
        obj65.draw.netForce(1)
        obj65.draw.enable(0)
        obj66.draw.netForce(1)
        obj66.draw.enable(0)
        obj67.draw.netForce(1)
        obj67.draw.enable(0)
        obj68.draw.netForce(1)
        obj68.draw.enable(0)
        obj69.draw.netForce(1)
        obj69.draw.enable(0)
        obj70.draw.netForce(1)
        obj70.draw.enable(0)
        obj71.draw.netForce(1)
        obj71.draw.enable(0)
        obj72.draw.netForce(1)
        obj72.draw.enable(0)
        obj73.draw.netForce(1)
        obj73.draw.enable(0)
        obj74.draw.netForce(1)
        obj74.draw.enable(0)
        obj75.draw.netForce(1)
        obj75.draw.enable(0)
        obj76.draw.netForce(1)
        obj76.draw.enable(0)
        obj77.draw.netForce(1)
        obj77.draw.enable(0)
        obj78.draw.netForce(1)
        obj78.draw.enable(0)
        obj79.draw.netForce(1)
        obj79.draw.enable(0)
        obj80.draw.netForce(1)
        obj80.draw.enable(0)
        obj81.draw.netForce(1)
        obj81.draw.enable(0)
        obj82.draw.netForce(1)
        obj82.draw.enable(0)
        obj83.draw.netForce(1)
        obj83.draw.enable(0)
        obj84.draw.netForce(1)
        obj84.draw.enable(0)
        obj85.draw.netForce(1)
        obj85.draw.enable(0)
        obj86.draw.netForce(1)
        obj86.draw.enable(0)
        obj87.draw.netForce(1)
        obj87.draw.enable(0)
        obj88.draw.netForce(1)
        obj88.draw.enable(0)
        obj89.draw.netForce(1)
        obj89.draw.enable(0)
        obj90.draw.netForce(1)
        obj90.draw.enable(0)
        obj91.draw.netForce(1)
        obj91.draw.enable(0)
        obj92.draw.netForce(1)
        obj92.draw.enable(0)
        obj93.draw.netForce(1)
        obj93.draw.enable(0)
        obj94.draw.netForce(1)
        obj94.draw.enable(0)
        obj95.draw.netForce(1)
        obj95.draw.enable(0)
        obj96.draw.netForce(1)
        obj96.draw.enable(0)
        obj97.draw.netForce(1)
        obj97.draw.enable(0)
        obj98.draw.netForce(1)
        obj98.draw.enable(0)
        obj99.draw.netForce(1)
        obj99.draw.enable(0)
        obj100.draw.netForce(1)
        obj100.draw.enable(0)
        obj101.draw.netForce(1)
        obj101.draw.enable(0)
        #obj102.draw.netForce(1)
        #obj102.draw.enable(0)
        obj103.draw.netForce(1)
        obj103.draw.enable(0)
        obj104.draw.netForce(1)
        obj104.draw.enable(0)
        obj105.draw.netForce(1)
        obj105.draw.enable(0)
        obj106.draw.netForce(1)
        obj106.draw.enable(0)
        obj107.draw.netForce(1)
        obj107.draw.enable(0)
        obj108.draw.netForce(1)
        obj108.draw.enable(0)
        obj109.draw.netForce(1)
        obj109.draw.enable(0)
        obj110.draw.netForce(1)
        obj110.draw.enable(0)
        obj111.draw.netForce(1)
        obj111.draw.enable(0)
        obj112.draw.netForce(1)
        obj112.draw.enable(0)
        obj113.draw.netForce(1)
        obj113.draw.enable(0)
        obj114.draw.netForce(1)
        obj114.draw.enable(0)
        obj115.draw.netForce(1)
        obj115.draw.enable(0)
        obj116.draw.netForce(1)
        obj116.draw.enable(0)
        obj117.draw.netForce(1)
        obj117.draw.enable(0)
        obj118.draw.netForce(1)
        obj118.draw.enable(0)
        obj119.draw.netForce(1)
        obj119.draw.enable(0)
        obj120.draw.netForce(1)
        obj120.draw.enable(0)
        obj121.draw.netForce(1)
        obj121.draw.enable(0)
        obj122.draw.netForce(1)
        obj122.draw.enable(0)
        obj123.draw.netForce(1)
        obj123.draw.enable(0)
        obj124.draw.netForce(1)
        obj124.draw.enable(0)
        obj125.draw.netForce(1)
        obj125.draw.enable(0)
        obj126.draw.netForce(1)
        obj126.draw.enable(0)
        obj127.draw.netForce(1)
        obj127.draw.enable(0)
        obj128.draw.netForce(1)
        obj128.draw.enable(0)
        obj129.draw.netForce(1)
        obj129.draw.enable(0)
        obj130.draw.netForce(1)
        obj130.draw.enable(0)
        obj131.draw.netForce(1)
        obj131.draw.enable(0)
        obj132.draw.netForce(1)
        obj132.draw.enable(0)
        #obj133.draw.netForce(1)
        #obj133.draw.enable(0)
        obj134.draw.netForce(1)
        obj134.draw.enable(0)
        obj135.draw.netForce(1)
        obj135.draw.enable(0)
        obj136.draw.netForce(1)
        obj136.draw.enable(0)
        obj137.draw.netForce(1)
        obj137.draw.enable(0)
        obj138.draw.netForce(1)
        obj138.draw.enable(0)
        obj139.draw.netForce(1)
        obj139.draw.enable(0)
        obj140.draw.netForce(1)
        obj140.draw.enable(0)
        obj141.draw.netForce(1)
        obj141.draw.enable(0)
        obj142.draw.netForce(1)
        obj142.draw.enable(0)
        obj143.draw.netForce(1)
        obj143.draw.enable(0)
        obj144.draw.netForce(1)
        obj144.draw.enable(0)
        obj145.draw.netForce(1)
        obj145.draw.enable(0)
        obj146.draw.netForce(1)
        obj146.draw.enable(0)
        obj147.draw.netForce(1)
        obj147.draw.enable(0)
        obj148.draw.netForce(1)
        obj148.draw.enable(0)
        obj149.draw.netForce(1)
        obj149.draw.enable(0)
        obj150.draw.netForce(1)
        obj150.draw.enable(0)
        obj151.draw.netForce(1)
        obj151.draw.enable(0)
        obj152.draw.netForce(1)
        obj152.draw.enable(0)
        obj153.draw.netForce(1)
        obj153.draw.enable(0)
        obj154.draw.netForce(1)
        obj154.draw.enable(0)
        obj155.draw.netForce(1)
        obj155.draw.enable(0)
        obj156.draw.netForce(1)
        obj156.draw.enable(0)
        obj157.draw.netForce(1)
        obj157.draw.enable(0)
        obj158.draw.netForce(1)
        obj158.draw.enable(0)
        obj159.draw.netForce(1)
        obj159.draw.enable(0)
        obj160.draw.netForce(1)
        obj160.draw.enable(0)
        obj161.draw.netForce(1)
        obj161.draw.enable(0)
        obj162.draw.netForce(1)
        obj162.draw.enable(0)
        obj163.draw.netForce(1)
        obj163.draw.enable(0)
        obj164.draw.netForce(1)
        obj164.draw.enable(0)
        obj165.draw.netForce(1)
        obj165.draw.enable(0)
        obj166.draw.netForce(1)
        obj166.draw.enable(0)
        obj167.draw.netForce(1)
        obj167.draw.enable(0)
        obj168.draw.netForce(1)
        obj168.draw.enable(0)
        obj169.draw.netForce(1)
        obj169.draw.enable(0)
        obj170.draw.netForce(1)
        obj170.draw.enable(0)
        obj171.draw.netForce(1)
        obj171.draw.enable(0)
        obj172.draw.netForce(1)
        obj172.draw.enable(0)
        obj173.draw.netForce(1)
        obj173.draw.enable(0)
        obj174.draw.netForce(1)
        obj174.draw.enable(0)
        obj175.draw.netForce(1)
        obj175.draw.enable(0)
        obj176.draw.netForce(1)
        obj176.draw.enable(0)
        obj177.draw.netForce(1)
        obj177.draw.enable(0)
        obj178.draw.netForce(1)
        obj178.draw.enable(0)
        obj179.draw.netForce(1)
        obj179.draw.enable(0)
        obj180.draw.netForce(1)
        obj180.draw.enable(0)
        obj181.draw.netForce(1)
        obj181.draw.enable(0)
        obj182.draw.netForce(1)
        obj182.draw.enable(0)
        obj183.draw.netForce(1)
        obj183.draw.enable(0)
        obj184.draw.netForce(1)
        obj184.draw.enable(0)
        obj185.draw.netForce(1)
        obj185.draw.enable(0)
        obj186.draw.netForce(1)
        obj186.draw.enable(0)
        obj187.draw.netForce(1)
        obj187.draw.enable(0)
        obj188.draw.netForce(1)
        obj188.draw.enable(0)
        obj189.draw.netForce(1)
        obj189.draw.enable(0)
        obj190.draw.netForce(1)
        obj190.draw.enable(0)
        obj191.draw.netForce(1)
        obj191.draw.enable(0)
        obj192.draw.netForce(1)
        obj192.draw.enable(0)
        obj193.draw.netForce(1)
        obj193.draw.enable(0)
        obj194.draw.netForce(1)
        obj194.draw.enable(0)
        obj195.draw.netForce(1)
        obj195.draw.enable(0)
        obj196.draw.netForce(1)
        obj196.draw.enable(0)
        obj197.draw.netForce(1)
        obj197.draw.enable(0)
        obj198.draw.netForce(1)
        obj198.draw.enable(0)
        obj199.draw.netForce(1)
        obj199.draw.enable(0)
        obj200.draw.netForce(1)
        obj200.draw.enable(0)   
        obj201.draw.netForce(1)
        obj201.draw.enable(0)
        obj202.draw.netForce(1)
        obj202.draw.enable(0)
        #obj203.draw.netForce(1)
        #obj203.draw.enable(0)
        obj204.draw.netForce(1)
        obj204.draw.enable(0)
        obj205.draw.netForce(1)
        obj205.draw.enable(0)
        obj206.draw.netForce(1)
        obj206.draw.enable(0)
        obj207.draw.netForce(1)
        obj207.draw.enable(0)
        obj208.draw.netForce(1)
        obj208.draw.enable(0)
        obj209.draw.netForce(1)
        obj209.draw.enable(0)
        obj210.draw.netForce(1)
        obj210.draw.enable(0)
        obj211.draw.netForce(1)
        obj211.draw.enable(0)
        obj212.draw.netForce(1)
        obj212.draw.enable(0)
        obj213.draw.netForce(1)
        obj213.draw.enable(0)
        #obj214.draw.netForce(1)
        #obj214.draw.enable(0)
        obj215.draw.netForce(1)
        obj215.draw.enable(0)
        obj216.draw.netForce(1)
        obj216.draw.enable(0)
        obj217.draw.netForce(1)
        obj217.draw.enable(0)
        obj218.draw.netForce(1)
        obj218.draw.enable(0)
        obj219.draw.netForce(1)
        obj219.draw.enable(0)
        obj220.draw.netForce(1)
        obj220.draw.enable(0)
        obj221.draw.netForce(1)
        obj221.draw.enable(0)
        obj222.draw.netForce(1)
        obj222.draw.enable(0)
        obj223.draw.netForce(1)
        obj223.draw.enable(0)
        obj224.draw.netForce(1)
        obj224.draw.enable(0)
        obj225.draw.netForce(1)
        obj225.draw.enable(0)
        obj226.draw.netForce(1)
        obj226.draw.enable(0)
        obj227.draw.netForce(1)
        obj227.draw.enable(0)
        obj228.draw.netForce(1)
        obj228.draw.enable(0)
        obj229.draw.netForce(1)
        obj229.draw.enable(0)
        obj230.draw.netForce(1)
        obj230.draw.enable(0)
        obj231.draw.netForce(1)
        obj231.draw.enable(0)
        obj232.draw.netForce(1)
        obj232.draw.enable(0)
        obj233.draw.netForce(1)
        obj233.draw.enable(0)
        obj234.draw.netForce(1)
        obj234.draw.enable(0)
        obj235.draw.netForce(1)
        obj235.draw.enable(0)
        obj236.draw.netForce(1)
        obj236.draw.enable(0)
        obj237.draw.netForce(1)
        obj237.draw.enable(0)
        obj238.draw.netForce(1)
        obj238.draw.enable(0)
        obj239.draw.netForce(1)
        obj239.draw.enable(0)
        obj240.draw.netForce(1)
        obj240.draw.enable(0)
        obj241.draw.netForce(1)
        obj241.draw.enable(0)
        obj242.draw.netForce(1)
        obj242.draw.enable(0)
        obj243.draw.netForce(1)
        obj243.draw.enable(0)
        obj244.draw.netForce(1)
        obj244.draw.enable(0)
        obj245.draw.netForce(1)
        obj245.draw.enable(0)
        obj246.draw.netForce(1)
        obj246.draw.enable(0)
        obj247.draw.netForce(1)
        obj247.draw.enable(0)
        obj248.draw.netForce(1)
        obj248.draw.enable(0)
        obj249.draw.netForce(1)
        obj249.draw.enable(0)
        obj250.draw.netForce(1)
        obj250.draw.enable(0)
        obj251.draw.netForce(1)
        obj251.draw.enable(0)
        obj252.draw.netForce(1)
        obj252.draw.enable(0)
        obj253.draw.netForce(1)
        obj253.draw.enable(0)
        obj254.draw.netForce(1)
        obj254.draw.enable(0)
        obj255.draw.netForce(1)
        obj255.draw.enable(0)
        obj256.draw.netForce(1)
        obj256.draw.enable(0)
        obj257.draw.netForce(1)
        obj257.draw.enable(0)
        obj258.draw.netForce(1)
        obj258.draw.enable(0)
        obj259.draw.netForce(1)
        obj259.draw.enable(0)
        print 'All undesired objects have been hide';

#class morehide:
#    def onAlarm(self,context):
#        import disable;disable.runDesert1();disable.runDesert2()
        