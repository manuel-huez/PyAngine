
from ..engine import Engine

class Keyboard:
	@staticmethod
	def isDown(key):
		keys = Engine.PyGame.key.get_pressed()
		return keys[key]

	@staticmethod
	def isUp(key):
		keys = Engine.PyGame.key.get_pressed()
		return not keys[key]
