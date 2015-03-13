# engine.sounds.soundmanager

from .sound import Sound
from ..engine import Engine

class SoundManager:
	def __init__(self):
		self._sounds = {}

	def load(self, name, path):
		newSound = Sound(path)
		self._sounds.update({name: newSound})

	def play(self, name):
		self._sounds[name].play()

	def stop(self, name):
		self._sounds[name].stop()
