from pyglet import *
from pyglet.window import *

class GameObject:
	def __init__(self, centerX, centerY, height, width):
		self.centerX = centerX
		self.centerY = centerY 
		self.height = height
		self.width = width

	def draw (self):
		raise Exception("dude, you're not drawing in ", self.__class__.__name__)

