
import pyglet
from pyglet.gl import *

import math



class Wimp :

	def __init__(self,monde):
		self.monde = monde
		self.camera = self.monde.camera
		self.enAvant     = False
		self.enArriere   = False
		self.versHaut    = False
		self.versBas     = False
		self.aGauche     = False
		self.aDroite     = False
		self.surgauche   = False
		self.surDroite   = False
		self.enableMouseMove = False
		self.rotationSpeed = 2

	def actualiser(self,dt):
		if self.enAvant :
			self.monde.guide.avancer(0.25)
		elif self.enArriere :
			self.monde.guide.avancer(-0.25)
		elif self.versHaut :
			self.monde.guide.monter(0.1)
		elif self.versBas :
			self.monde.guide.monter(-0.1)
		elif self.aGauche :
			self.monde.guide.gauche(0.25)
		elif self.aDroite :
			self.monde.guide.gauche(-0.25)

		else:
			pass

	def on_key_press(self,symbol):
		if symbol == pyglet.window.key.SPACE :
			pass
		elif symbol == pyglet.window.key.UP :
			self.enAvant = True
		elif symbol == pyglet.window.key.DOWN :
			self.enArriere = True
		elif symbol == pyglet.window.key.LEFT :
			self.aGauche = True
		elif symbol == pyglet.window.key.RIGHT :
			self.aDroite = True
                elif symbol == pyglet.window.key.Z :
			self.enAvant = True
		elif symbol == pyglet.window.key.S :
			self.enArriere = True
		elif symbol == pyglet.window.key.Q :
			self.aGauche = True
		elif symbol == pyglet.window.key.D :
			self.aDroite = True
		elif symbol == pyglet.window.key.H :
			self.versHaut = True
		elif symbol == pyglet.window.key.B :
			self.versBas  = True
		elif symbol == pyglet.window.key.T :
			self.monde.notifier()
		else:
			pass

	def on_key_release(self,symbol):
		if symbol == pyglet.window.key.SPACE :
			pass
		elif symbol == pyglet.window.key.UP :
			self.enAvant = False
		elif symbol == pyglet.window.key.DOWN :
			self.enArriere=False
		elif symbol == pyglet.window.key.LEFT :
			self.aGauche = False
		elif symbol == pyglet.window.key.RIGHT :
			self.aDroite = False
                elif symbol == pyglet.window.key.Z :
			self.enAvant = False
		elif symbol == pyglet.window.key.S :
			self.enArriere=False
		elif symbol == pyglet.window.key.Q :
			self.aGauche = False
		elif symbol == pyglet.window.key.D :
			self.aDroite = False
		elif symbol == pyglet.window.key.H :
			self.versHaut = False
		elif symbol == pyglet.window.key.B :
			self.versBas  = False
		elif symbol == pyglet.window.key.F :
			if self.camera.dist == 3 :
				self.camera.dist = 0
			else :
				self.camera.dist = 3
		else:
			pass

	def on_mouse_press(self,x,y,bouton,modifiers):
		pass

	def on_mouse_release(self,x,y,bouton,modifiers):
		self.enableMouseMove = (self.enableMouseMove == False)

	def on_mouse_drag(self,x,y,dx,dy):
		#print "DX = ", dx
		if dx < -1 :
			self.monde.guide.tourner(2*math.pi/180.0)
		elif dx > 1 :
			self.monde.guide.tourner(-2*math.pi/180.0)
	def on_mouse_motion(self,x,y,dx,dy):
		return
		if self.enableMouseMove:
			#print "DX = ", dx
			if dx < -1 : 
				self.camera.tourner(2*math.pi/180.0 * self.rotationSpeed)
			elif dx > 1 : 
				self.camera.tourner(-2*math.pi/180.0 * self.rotationSpeed)			

