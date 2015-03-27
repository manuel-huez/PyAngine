# engine.scene

from .sounds.soundmanager import SoundManager
from .engine import Engine

class Scene:
	def __init__(self):
		self._soundManager = SoundManager()
		self._objects      = {}

	def addObject(self, key, obj):
		if(key in self._objects):
			self._objects[key] = obj
		else:
			self._objects.update({key: obj})

	def getObject(self, key):
		if(key in self._objects):
			return self._objects[key]
		return None

	def removeObject(self, key):
		if(key in self._objects):
			del self._objects[key]

	@property
	def soundManager(self):
		return self._soundManager

	def set(self):
		return True

	def unset(self):
		return True

	def update(self, dt):
		return True

	def draw(self, dt):
		Engine.Screen.fill(Engine.BackgroundColor)

		for obj in self._objects.values():
			if(obj.surface == None):
				continue
			Engine.Screen.blit(obj.surface, obj.rectangle)

		Engine.PyGame.display.flip()
