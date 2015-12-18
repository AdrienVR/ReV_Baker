# -*- coding: utf-8 -*-

import geo
import visu
import math
import graphe


class Monde :

  def __init__(self):
    self.horloge = 0.0
    self.camera = visu.Camera()
    self.decor  = []
    self.transparentDecor  = []
    self.activites = []
    self.annuaire = {}
    self.visiteur = visu.Objet()
    self.fabrique = None

  def dessiner(self):
    self.camera.lookAt()
    for x in self.decor :
      x.dessiner()
    for x in self.transparentDecor :
      x.dessiner()

  def actualiser(self,dt):
    self.horloge += dt
    for x in self.activites :
	x.actualiser(self.horloge,dt)

  def ajouter(self,decor=None,activite=None):
    if decor != None :
      self.decor.append(decor)
    if activite != None :
      self.activites.append(activite)

  def ajouterTransparent(self,decor=None):
    if decor != None :
      self.transparentDecor.append(decor)

  def enregistrer(self,nom,obj):
    self.annuaire[nom] = obj




class Activite :

  def __init__(self,id=None,objet=None):
    self.id = id
    self.actif = False
    self.objet = objet

  def start(self):
    self.actif = True

  def stop(self):
    self.actif = False

  def pause(self):
    self.actif = False

  def actualiser(self,t,dt):
    pass

class ActiviteVisiteur(Activite) :

    def __init__(self,id=None,objet=None,camera=visu.Camera()):
        Activite.__init__(self, id, objet)
        self.cam = camera
        self.dernier_etat="hors_escalier"
        self.etat = "hors_escalier"

    def actualiser(self,t,dt):
        self.cam.orienter(self.objet.repere.angle)
        self.objet.orienter(self.objet.repere.angle)
        xCam = self.objet.repere.o.x - self.cam.dist*math.cos(self.objet.repere.angle)
        yCam = self.objet.repere.o.y - self.cam.dist*math.sin(self.objet.repere.angle)

        z = self.objet.repere.o.z
        if self.objet.repere.o.x>= 5.1 and self.objet.repere.o.x<= 7.7 and self.objet.repere.o.y >= 5.1 and self.objet.repere.o.y<=10.2 and self.objet.repere.o.z <= 2.8:
            z=0.1+(2.8-0.1)*(self.objet.repere.o.y-5.1)/(10.2-5.1)
            self.objet.placer(geo.Vec3((self.objet.repere.o.x,self.objet.repere.o.y,z)))

        if self.objet.repere.o.x>= 7.2 and self.objet.repere.o.x<= 7.88 and self.objet.repere.o.y <= 16.4 and self.objet.repere.o.y>=16.16 :
            self.etat = "zone_escalier2_bas"
        if self.objet.repere.o.x>= 4.76 and self.objet.repere.o.x<= 5.61 and self.objet.repere.o.y <= 16.67 and self.objet.repere.o.y>=16.55 :
            self.etat = "zone_escalier2_haut"
        if self.dernier_etat == "zone_escalier2_bas" :
            if self.objet.repere.o.y >= 16.4 :
                self.etat = "escalier2"
            elif self.objet.repere.o.y <= 16.16 :
                self.etat = "hors_escalier"
                z=2.8
                self.objet.placer(geo.Vec3((self.objet.repere.o.x,self.objet.repere.o.y,z)))
        if self.dernier_etat == "zone_escalier2_haut" :
            if self.objet.repere.o.y >= 16.67 :
                self.etat = "escalier2"
            elif self.objet.repere.o.y <= 16.55 :
                self.etat = "hors_escalier"
                z=5.1
                self.objet.placer(geo.Vec3((self.objet.repere.o.x,self.objet.repere.o.y,z)))
        self.dernier_etat = self.etat

        if self.etat == "escalier2" :
            z=2.8+(5.1-2.8)*(7.88-self.objet.repere.o.x)/(7.88-5.61)
            if self.objet.repere.o.x >= 7.5 and self.objet.repere.o.x < 8 :
                y = 16.3
            elif self.objet.repere.o.x >= 6.2 and self.objet.repere.o.x < 7.5 :
                y = 17.59
            elif self.objet.repere.o.x >= 5 and self.objet.repere.o.x < 6.2 :
                y = 16.60
            else :
                y = 16.60
            self.objet.placer(geo.Vec3((self.objet.repere.o.x,y,z)))
            print self.objet.repere.o.x

        self.cam.placer(geo.Vec3((xCam,yCam,self.objet.repere.o.z+0.8)))

class ActiviteGuide(Activite) :

    def __init__(self,id=None,objet=None,visiteur=None):
        Activite.__init__(self, id, objet)
        self.etat = "aller"
        self.visiteur = visiteur

        self.graphe = graphe.lireGrapheNavigation("graphe.nav")
    	self.dij = graphe.Dijkstra(self.graphe)
        self.noeudCourant = "entree_rdc_1" #self.graphe.premierSommet()
        print "noeud initial : " + self.noeudCourant
        self.objet.placer(geo.Vec3((self.graphe.etiquette(self.noeudCourant).x,self.graphe.etiquette(self.noeudCourant).y,self.graphe.etiquette(self.noeudCourant).z)))
        self.objet.orienter(math.pi/2)

        self.noeudCible = "salle2_f2_couloirb"
        self.parcoursListe = self.dij.trouverChemin(de=self.noeudCourant,a=self.noeudCible)
        self.posList = 0
        self.pointCible = self.parcoursListe[1]
        print self.parcoursListe
        self.pointCible.y = self.pointCible.y + 1
        #print "posX = " + str(self.objet.repere.o.x) + " posY = " + str(self.objet.repere.o.y)+ " cibleX = " + str(self.pointCible.x) + " cibleY = " + str(self.pointCible.y)

    def actualiser(self,t,dt):
        if self.etat == "aller" :
            dr=dt*0.5
            atteint = False

            xc = self.objet.repere.o.x - self.pointCible.x
            yc = self.objet.repere.o.y - self.pointCible.y

            r = math.sqrt(xc*xc + yc*yc)
            if xc > 0 : theta = math.atan(yc/xc)
            elif xc == 0 and yc > 0 : theta = math.pi/2.0
            elif xc == 0 and yc < 0 : theta = -1.0* math.pi/2
            elif xc == 0 and yc == 0 : theta = 0
            elif yc >= 0 : theta = math.atan(yc/xc) + math.pi
            elif yc < 0 : theta = math.atan(yc/xc) - math.pi

            if r>dr :
                r = r-dr
            else :
                atteint = True

            xc = r*math.cos(theta)
            yc = r*math.sin(theta)

            if math.fabs(self.objet.repere.o.z-self.pointCible.z) > dr :
                if self.objet.repere.o.z >= self.pointCible.z : dz = -0.5*dr
                else : dz = 0.5*dr
                atteint = False
            else :
                dz = 0


            self.objet.placer(geo.Vec3((xc+self.pointCible.x,yc+self.pointCible.y,dz+self.objet.repere.o.z)))

            if self.objet.repere.angle > theta+1.1*math.pi : self.objet.orienter(self.objet.repere.angle-math.pi/30.0)
            elif self.objet.repere.angle < theta+0.9*math.pi : self.objet.orienter(self.objet.repere.angle+math.pi/30.0)
            #print self.objet.repere.angle

            #self.objet.orienter(theta+math.pi)

            if atteint :
                self.posList += 1
                if self.posList + 1 >= len(self.parcoursListe) :
                    self.etat = "attendre"
                else :
                    self.pointCible = self.parcoursListe[self.posList+1]

        elif self.etat == "attendre" :
            #print "attendre"
            pass

            #print "posX = " + str(self.objet.repere.o.x) + " posY = " + str(self.objet.repere.o.y)+ " cibleX = " + str(self.pointCible.x) + " cibleY = " + str(self.pointCible.y)


#    if self.actif :
 #     print "ACTIVITE : ", t, " - ", dt
