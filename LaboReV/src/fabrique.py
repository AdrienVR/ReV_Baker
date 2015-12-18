# -*- coding: utf-8 -*-

import math
import geo
import visu
import simu

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

    self.emplacements_tableaux = {
        "A1" : (4.55, 1.5, 0.3, "../data/images/Automobile/Amicar.jpg"),
        "A2" : (3.15, 0.98, 0.3, "../data/images/Automobile/Autobus.jpg"),
    }
    self.tableaux = {}


    self.transparentMaison = {
		"rdc/transparent_rdc" : (0, 0, self.rdcheight),

		"f1/eau_f1_transparent" : (2, 6, self.f1height),
		"f1/transparent_f1" : (0, 0, self.f1height),
	}

    self.maisonModels = {}
    self.monde = le_monde

  def fabriquer(self):

    le_sol = visu.Objet(maillage=visu.Sol())
    self.monde.ajouter(decor=le_sol)

    le_ciel = visu.Objet(maillage = visu.Ciel())
    self.monde.ajouterTransparent(decor=le_ciel)

    for emplacement_tableau in self.emplacements_tableaux.keys() :
        self.tableaux[emplacement_tableau] = visu.Objet(maillage=visu.Tableau(recto=self.emplacements_tableaux[emplacement_tableau][3],\
                                                      verso=self.emplacements_tableaux[emplacement_tableau][3],\
                                                      largeur=1.0,hauteur=1.0,epaisseur=0.1))
        self.tableaux[emplacement_tableau].placer(geo.Vec3((self.emplacements_tableaux[emplacement_tableau][0],self.emplacements_tableaux[emplacement_tableau][1],self.emplacements_tableaux[emplacement_tableau][2])))
        self.monde.ajouter(decor=self.tableaux[emplacement_tableau])

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
