# -*- coding: utf-8 -*-

import math
import geo
import visu
import simu

class Fabrique :

  def __init__(self,le_monde):
    self.maison = {
##	"rdc/garage_rdc" : (2, 18, 0),
##	"rdc/cave1_rdc" : (4, 13,5, 0),
##	"rdc/cave2_rdc" : (10, 13, 0),
##	"rdc/couloir_rdc" : (4, 11,5, 0),
##	"rdc/chambre1_rdc" : (1, 6,5, 0),
##	"rdc/chambre2_rdc" : (1, 9,5, 0),
##	"rdc/chambre3_rdc" : (1, 13,5, 0),
##	"rdc/cuisine_rdc" : (1, 3,5, 0),
##	"rdc/salle1_rdc" : (2, 1,5, 0),
##	"rdc/salle2_rdc" : (3,5, 1,5, 0),
##	"rdc/entree_rdc" : (6, 3, 0),
##	"rdc/concierge_rdc" : (7,5, 2, 0),

	"f1/sol_f1" : (0, 0, 2.3),
	"f1/sol_f1" : (0, 0, 2.3),
	"f1/couloir_f1" : (0, 0, 2.3),
	"f1/salon_f1" : (2, 15, 2.3),
	"f1/eau_f1" : (2, 6, 2.3),
	"f1/petitSalon_f1" : (0, 0, 2.3),
	"f1/cafe_f1" : (6, 2, 2.3),
	"f1/salle1_f1" : (10, 19, 2.3),

	"f2/sol_f2" : (0, 0, 4.6),
	"f2/piscine_f2" : (0, 0, 4.6),
	"f2/salles_f2" : (3, 15, 4.6),
	"f2/couloir_f2" : (8, 16, 4.6),
	"f2/manger_f2" : (7.5, 6, 4.6)
    }
    self.maisonModels = {}
    self.monde = le_monde

  def fabriquer(self):

    le_sol = visu.Objet(maillage=visu.Sol())
    self.monde.ajouter(decor=le_sol)

    le_ciel = visu.Objet(maillage = visu.Ciel())
    self.monde.ajouter(decor=le_ciel)

    #le_tableau = visu.Objet(maillage=visu.Tableau(recto="../data/textures/gris.jpg",\
    #                                              verso="../data/textures/Ceramic.jpg",\
    #                                              largeur=2.0,hauteur=3.0,epaisseur=0.1))
    #le_tableau.placer(geo.Vec3((0.0,0.0,2.0)))
    #self.monde.ajouter(decor=le_tableau)

    #le_tableau = visu.Objet(maillage=visu.Panneau(recto="../data/textures/tree1.png",\
    #                                              verso="../data/textures/tree1.png",\
    #                                              largeur=6.0,hauteur=12.0,epaisseur=0.1))
    #le_tableau.placer(geo.Vec3((5.0,5.0,0.0)))
    #self.monde.ajouter(decor=le_tableau)

    for piece in self.maison.keys():
      self.maisonModels[piece] = visu.Objet(maillage=visu.ObjY(url="../data/baker/"+piece+".obj"))
      self.maisonModels[piece].placer(geo.Vec3((self.maison[piece])))
      self.monde.ajouter(decor=self.maisonModels[piece])

    le_pingouin = visu.Objet(maillage=visu.Obj(url="../data/obj/pingouin/p.obj"))
    le_pingouin.placer(geo.Vec3((-2.0,3.0,0.0)))
    le_pingouin.orienter(45.0*math.pi/180.0)
    self.monde.ajouter(decor=le_pingouin)

    une_activite = simu.Activite(id="act-01")
    une_activite.start()
    self.monde.ajouter(activite=une_activite)
