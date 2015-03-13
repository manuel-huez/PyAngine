
from engine.engine           import Engine
from engine.scene            import Scene
from engine.actions.keyboard import Keyboard
from engine.misc.console     import Console

class DefaultScene(Scene):
	def __init__(self):
		super(DefaultScene, self).__init__()

	def update(self, dt):
		player      = Engine.SceneManager.scene.getObject('player')
		oldPosition = player.position

		if(Keyboard.isDown(Engine.PyGame.K_a)):
			Console.info('left')
			player.positionX -= 0.1 * dt
		if(Keyboard.isDown(Engine.PyGame.K_d)):
			Console.info('right')
			player.positionX += 0.1 * dt
		if(Keyboard.isDown(Engine.PyGame.K_w)):
			Console.info('top')
			player.positionY -= 0.1 * dt
		if(Keyboard.isDown(Engine.PyGame.K_s)):
			Console.info('bottom')
			player.positionY += 0.1 * dt
