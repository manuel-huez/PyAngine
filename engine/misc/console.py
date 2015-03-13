# engine.misc.console

from ..engine import Engine

class ConsoleColors:
	HEADER    = '\033[95m'
	OKBLUE    = '\033[94m'
	OKGREEN   = '\033[92m'
	WARNING   = '\033[93m'
	FAIL      = '\033[91m'
	ENDC      = '\033[0m'
	BOLD      = '\033[1m'
	UNDERLINE = '\033[4m'

class Console:
	_enabled = False

	@staticmethod
	def enable():
		Console._enabled = True

	@staticmethod
	def disable():
		Console._enabled = False

	@staticmethod
	def header(text):
		print(ConsoleColors.HEADER +  '[HEADER] '  + text)

	@staticmethod
	def info(text):
		print(ConsoleColors.OKBLUE +  '[INFO] '    + text)

	@staticmethod
	def success(text):
		print(ConsoleColors.OKGREEN + '[SUCCESS] ' + text)

	@staticmethod
	def warning(text):
		print(ConsoleColors.WARNING + '[WARNING] ' + text)

	@staticmethod
	def error(text):
		print(ConsoleColors.FAIL +    '[FAIL] '    + text)
