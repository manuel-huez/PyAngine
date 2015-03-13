# engine.sounds.sound

import os
from ..engine import Engine

class Sound:
	def __init__(self, path):
		self._sound = Engine.PyGame.mixer.Sound(os.path.join(path))

	def play(self):
		self._sound.play()

	def stop(self):
		self._sound.stop()
