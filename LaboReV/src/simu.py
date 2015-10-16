
import geo
import visu


class Monde :
  
  def __init__(self):
    self.horloge = 0.0
    self.camera = visu.Camera()
    self.decor  = []
    self.activites = []
    self.annuaire = {}
    
  def dessiner(self):
    self.camera.lookAt()
    for x in self.decor :
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
    if self.actif : 
      print "ACTIVITE : ", t, " - ", dt
    