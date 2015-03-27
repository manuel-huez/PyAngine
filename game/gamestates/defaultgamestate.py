
from engine.gamestate import GameState
from engine.misc.console import Console

class DefaultGameState(GameState):
	def __init__(self):
		super(DefaultGameState, self).__init__()

	def set(self):
		Console.success('default game state loaded')
