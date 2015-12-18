# -*- coding: utf-8 -*-

import math
import geo
import visu
import simu
import glob, os
from random import randint

class Fabrique :

  def __init__(self,le_monde):

    self.rdcheight = 0.1
    self.f1height = self.rdcheight + 2.6
    self.f2height = self.f1height + 2.3

    self.maison = {
	"rdc/garage_rdc" : (2, 18, self.rdcheight),
	"rdc/cave1_rdc" : (4, 13.5, self.rdcheight),
	"rdc/cave2_rdc" : (10, 19, self.rdcheight),
	"rdc/couloirs_rdc" : (4, 11.5, self.rdcheight),
	"rdc/chambre1_rdc" : (1, 6.5, self.rdcheight),
	"rdc/chambre2_rdc" : (1, 9.5, self.rdcheight),
	"rdc/chambre3_rdc" : (1, 13.5, self.rdcheight),
	"rdc/concierge_rdc" : (7.5, 2, self.rdcheight),
	"rdc/cuisine_rdc" : (1, 3.5, self.rdcheight),
	"rdc/salle1_rdc" : (2, 1.5, self.rdcheight),
	"rdc/salle2_rdc" : (3.5, 1.5, self.rdcheight),
	"rdc/entree_rdc" : (6, 3, self.rdcheight),

	"f1/sol_f1" : (0, 0, self.f1height),
	"f1/couloir_f1" : (0, 0, self.f1height),
	"f1/salon_f1" : (2, 15, self.f1height),
	"f1/eau_f1" : (2, 6, self.f1height),
	"f1/petitSalon_f1" : (0, 0, self.f1height),
	"f1/cafe_f1" : (6, 2, self.f1height),
	"f1/salle1_f1" : (10, 19, self.f1height),

	"f2/sol_f2" : (0, 0, self.f2height),
	"f2/piscine_f2" : (0, 0, self.f2height),
	"f2/salles_f2" : (3, 15, self.f2height),
	"f2/couloir_f2" : (8, 16, self.f2height),
	"f2/manger_f2" : (6, 4.4, self.f2height),
	"f2/plafond_f2" : (0, 0, self.f2height + 2),
    }

    self.tableauCoord = [(4.05,1.5,0.3),
(2.65,0.98,0.3),
(-1.35,1.34,0.3),
(-1.35,4.35,0.3),
(1.51,5.06,0.3),
(0.56,5.27,0.3),
(-1.35,7.37,0.3),
(1.48,8.03,0.3),
(3.02,5.98,0.3),
(1.71,8.23,0.3),
(-0.22,8.23,0.3),
(1.44,9.93,0.3),
(-0.17,15.12,0.3),
(-1.35,12.76,0.3),
(1.16,13.67,0.3),
(1.36,12.73,0.3),
(1.36,12.73,0.3),
(2.87,15.10,0.3),
(5.45,14.07,0.3),
(9.03,19.86,0.3),
(0.11,19.86,0.3),
(2.95,19.86,0.3),
(2.95,15.27,0.3),
(0.11,15.27,0.3),
(1.2,20.00,3.2),
(3.35,19.12,3.2),
(3.87,20.00,3.2),
(9.36,18.21,3.2),
(9.27,19.97,3.2),
(7.52,15.63,3.2),
(7.52,13.80,3.2),
(7.52,12.32,3.2),
(7.52,10.25,3.2),
(3.16,4.17,3.2),
(3.16,5.99,3.2),
(3.16,8.70,3.2),
(7.55,1.67,3.2),
(4.1,3.03,3.2),
(-0.62,-0.00,3.2),
(9.28,20.06,5.3),
(10.79,19.11,5.3),
(9.27,18.24,5.3),
(5.92,19.18,5.3),
(4.37,14.50,5.3),
(4.37,12.77,5.3),
(7.56,14.89,5.3),
(7.56,12.75,5.3),
(7.56,9.28,5.3),
(7.56,7.23,5.3),
(7.56,4.85,5.3),
(4.34,4.99,5.3),
(4.08,5.76,5.3),
(4.08,3.76,5.3),
(1.54,0.16,5.3),
(-1.37,2.01,5.3),
(-1.37,5.06,5.3),
(-1.37,8.25,5.3),
(1.33,15.99,5.3),
(1.36,16.09,5.3),
                          (1.83,15.99,4.9),
                          (1.83,15.99,4.9),
                          (1.83,15.99,4.9),
                          (1.86,16.09,4.9)]

    self.rotationTab = [0,0,1.57,1.57,0,0,1.57,0,1.57,0,0,0,0,0,1.57,1.57,1.57,0,1.57,0,0,0,0,0,
                        0,0,0,0,0,1.57,1.57,1.57,1.57,1.57,1.57,1.57,1.57,1.57,0,0,1.57,0,0,1.57,1.57,1.57,1.57,1.57,
                        1.57,1.57,1.57,1.57,1.57,0,1.57,1.57,1.57,0,1.57,1.57,1.57,1.57,1.57]

    self.textureNames = []


    self.tableaux = []

    self.transparentMaison = {
		"rdc/transparent_rdc" : (0, 0, self.rdcheight),

		"f1/eau_f1_transparent" : (2, 6, self.f1height),
		"f1/transparent_f1" : (0, 0, self.f1height),
	}

    self.maisonModels = {}
    self.monde = le_monde
    le_monde.fabrique = self

  def fabriquer(self):

    le_sol = visu.Objet(maillage=visu.Sol())
    self.monde.ajouter(decor=le_sol)

    le_ciel = visu.Objet(maillage = visu.Ciel())
    self.monde.ajouterTransparent(decor=le_ciel)

    os.chdir("../data/images")

    for directory in ("Automobile", "Loisirs", "Mode", "Politique", "Spectacle", "Sport", "Tableaux"):
      os.chdir(directory)
      for file in glob.glob("*.jpg"):
          self.textureNames.append(directory + "/"+ file)
      os.chdir("..")

    os.chdir("../../src")

    print len(self.textureNames), len(self.tableauCoord)
    for indexTableau in range(len(self.textureNames)) :
        self.tableaux.append(visu.Objet(maillage=visu.Tableau(recto="../data/images/" + self.textureNames[indexTableau],\
                                                      verso="../data/images/" +self.textureNames[indexTableau],\
                                                      largeur=1.0,hauteur=1.0,epaisseur=0.1)))
        self.tableaux[indexTableau].orienter(self.rotationTab[indexTableau])
        if (self.rotationTab[indexTableau] != 0):
          self.tableauCoord[indexTableau] = (self.tableauCoord[indexTableau][0] + 0.5,self.tableauCoord[indexTableau][1]- 0.5, self.tableauCoord[indexTableau][2])
        self.tableaux[indexTableau].placer(geo.Vec3(self.tableauCoord[indexTableau]))
        self.monde.ajouter(decor=self.tableaux[indexTableau])

    for piece in self.maison.keys():
      self.maisonModels[piece] = visu.Objet(maillage=visu.ObjY(url="../data/baker/"+piece+".obj"))
      self.maisonModels[piece].placer(geo.Vec3((self.maison[piece])))
      self.monde.ajouter(decor=self.maisonModels[piece])

    for piece in self.transparentMaison.keys():
      self.maisonModels[piece] = visu.ObjetBougeant(maillage=visu.ObjY(url="../data/baker/"+piece+".obj"))
      self.maisonModels[piece].placer(geo.Vec3((self.transparentMaison[piece])))
      self.monde.ajouterTransparent(decor=self.maisonModels[piece])

    le_visiteur = visu.Objet(maillage=visu.Obj(url="../data/obj/pingouin/p.obj"))
    le_visiteur.placer(geo.Vec3((6.6,-0.5,0.1)))
    le_visiteur.orienter(90*math.pi/180.0)
    self.monde.ajouter(decor=le_visiteur)
    suivi_visiteur = simu.ActiviteVisiteur(id="visite_pingouin", objet=le_visiteur, camera=self.monde.camera)
    suivi_visiteur.start()
    self.monde.ajouter(activite=suivi_visiteur)
    self.monde.visiteur = le_visiteur

    le_guide = visu.Objet(maillage=visu.Obj(url="../data/obj/pingouin/p.obj"))
    #le_guide.placer(geo.Vec3((6.3,1.1,0.1)))
    #le_guide.orienter(90*math.pi/180.0)
    self.monde.ajouter(decor=le_guide)
    deplacements_guide = simu.ActiviteGuide(id="guide_pingouin", objet=le_guide, visiteur=le_visiteur)
    deplacements_guide.start()
    self.monde.ajouter(activite=deplacements_guide)
    #self.monde.visiteur = le_visiteur

    #une_activite = simu.Activite(id="act-01")
    #une_activite.start()
    #self.monde.ajouter(activite=une_activite)

  def changeTableaux(self):
        m_index = randint(0, 61)
        for indexTableau in range(len(self.tableaux)) :
            textureIndex = (indexTableau + m_index)%len(self.textureNames)
            self.tableaux[indexTableau].maillage.changeTexture("../data/images/" + self.textureNames[textureIndex])
        print "changement des tableaux effectué"
