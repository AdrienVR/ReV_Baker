# -*- coding: utf-8 -*-

import geo
import visu
import math


class Monde :

  def __init__(self):
    self.horloge = 0.0
    self.camera = visu.Camera()
    self.decor  = []
    self.transparentDecor  = []
    self.activites = []
    self.annuaire = {}
    self.guide = visu.Objet()

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

class ActiviteGuide(Activite) :

    def __init__(self,id=None,objet=None,camera=visu.Camera()):
        Activite.__init__(self, id, objet)
        self.cam = camera

    def actualiser(self,t,dt):
        #self.objet.placer(geo.Vec3((-2.0+t,3.0+t*t,0.0)))
        #self.objet.orienter(t)
        self.cam.orienter(self.objet.repere.angle)
        xCam = self.objet.repere.o.x - self.cam.dist*math.cos(self.objet.repere.angle)
        yCam = self.objet.repere.o.y - self.cam.dist*math.sin(self.objet.repere.angle)
        self.cam.placer(geo.Vec3((xCam,yCam,self.objet.repere.o.z+1.0)))
        print(-2.0+t)

#    if self.actif :
 #     print "ACTIVITE : ", t, " - ", dt
