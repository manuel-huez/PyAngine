# engine.scenemanager

from .scene import Scene

class SceneManager:
	def __init__(self):
		self._currentScene = 'init'
		self._scenes       = {'init': Scene() }

	@property
	def scene(self):
		return self._scenes[self._currentScene]

	def setScene(self, name):
		self._currentScene = name

	def addScene(self, name, scene):
		self._scenes.update({name: scene})
		self._currentScene        = name

	def draw(self):
		self._scenes[self._currentScene].draw()
