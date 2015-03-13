# engine.physics.object

import os
from pygame.sprite import Sprite
from ..engine import Engine

class Object:
	def __init__(self, position, dimensions, collidable):
		super().__init__()
		self._posX        = position[0]
		self._posY        = position[1]
		self._width       = dimensions[0]
		self._height      = dimensions[1]
		self._collidable  = collidable
		self._surface     = None
		self._rect        = None
		self._sprite      = None

	@property
	def image(self):
		return self._surface

	def setImage(self, imagePath):
		image = Engine.PyGame.image.load(os.path.join(imagePath))
		image.convert()
		image              = Engine.PyGame.transform.scale(image,
			(self._width, self._height))
		self._surface      = image
		self._rect         = image.get_rect()
		self._sprite       = Sprite()
		self._sprite.image = self._surface
		self.updateRect()

	def updateRect(self):
		self._rect.x      = self._posX
		self._rect.y      = self._posY
		self._sprite.rect = self._rect

	@property
	def surface(self):
		return self._surface

	@property
	def sprite(self):
		return self._sprite

	@property
	def position(self):
		return (self._posX, self._posY)

	@position.setter
	def position(self, position):
		self._posX = position[0]
		self._posY = position[1]
		self.updateRect()

	@property
	def positionX(self):
		return self._posX

	@positionX.setter
	def positionX(self, x):
		self._posX = x
		self.updateRect()

	@property
	def positionY(self):
		return self._posY

	@positionY.setter
	def positionY(self, y):
		self._posY = y
		self.updateRect()

	@property
	def rectangle(self):
		return self._rect

	@property
	def dimensions(self):
		return (self._width, self._height)

	@dimensions.setter
	def dimensions(self, dimensions):
		self._width  = dimensions[0]
		self._height = dimensions[1]
