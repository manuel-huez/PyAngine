# engine.gamestatemanager

from .gamestate import GameState

class GameStateManager:
	def __init__(self):
		self._currentGameState = GameState()

	def set(self, gamestate):
		self._currentGameState.unset()
		self._currentGameState = gamestate
		self._currentGameState.set()
