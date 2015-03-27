# engine.engine

from datetime import datetime
from .decorators.classproperty import classproperty
import pygame

class Engine:
	_pygame          = None
	_screen          = None
	_basicfont       = None
	_frames          = None
	_backgroundcolor = None

	_scenemanager     = None
	_gamestatemanager = None
	_clock            = None

	@staticmethod
	def init(gameName, screenSize, fontFamily, fontSize, frames, backgroundColor,
			sceneManager, gameStateManager):
		pygame.init()
		pygame.display.set_caption(gameName)
		screen    = pygame.display.set_mode(screenSize)
		basicfont = pygame.font.SysFont(fontFamily, fontSize)

		Engine._pygame          = pygame
		Engine._screen          = screen
		Engine._basicfont       = basicfont
		Engine._frames          = frames
		Engine._backgroundcolor = backgroundColor

		Engine._scenemanager     = sceneManager
		Engine._gamestatemanager = gameStateManager
		Engine._clock            = Engine.PyGame.time.Clock()

	@classproperty
	def PyGame(cls):
		return cls._pygame

	@classproperty
	def Screen(cls):
		return cls._screen

	@classproperty
	def BasicFont(cls):
		return cls._basicfont

	@classproperty
	def Frames(cls):
		return cls._frames

	@classproperty
	def BackgroundColor(cls):
		return cls._backgroundcolor

	@classproperty
	def SceneManager(cls):
		return cls._scenemanager

	@classproperty
	def GameStateManager(cls):
		return cls._gamestatemanager

	@classproperty
	def Clock(cls):
		return cls._clock

	@staticmethod
	def tick():
		return Engine.Clock.tick(Engine.Frames)

	@staticmethod
	def run():
		dt = Engine.tick()
		Engine.update(dt)
		Engine.draw(dt)
		return dt

	@staticmethod
	def update(dt):
		Engine.SceneManager.scene.update(dt)

	@staticmethod
	def draw(dt):
		Engine.SceneManager.scene.draw(dt)
