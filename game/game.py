# game.game

import sys
import pygame
from engine.engine            import Engine
from engine.scene             import Scene
from engine.scenemanager      import SceneManager
from .scenes.defaultscene     import DefaultScene
from engine.physics.object    import Object
from engine.actions.keyboard  import Keyboard
from engine.misc.console      import Console

def startGame():
	Engine.init('Amazing game', (640, 480), None, 48, 60,
		(0, 0, 0), SceneManager())

	Engine.SceneManager.addScene('default', DefaultScene())

	player = Object((10, 10), (100, 100), True)
	player.setImage('Player.png')
	Engine.SceneManager.scene.addObject('player', player)

	Engine.SceneManager.scene.soundManager.load('bg', 'music.wav')
	#Engine.SceneManager.scene.soundManager.play('bg')

	Console.enable()

	while 1:
		for event in Engine.PyGame.event.get():
			if event.type == pygame.QUIT:
				Engine.PyGame.display.quit()
				sys.exit()

		dt = Engine.run()
