class Player:
	
	def __init__(self, player):
		self.name = input("Enter your name: ")
		self.player = player

	def setMove(self):
		while True:
			move = input("Enter your move: ")		
			try:
				initPos, endPos = move.split(', ')
				if self.validateMove(initPos) and self.validateMove(endPos):
					self.initPos = initPos
					self.endPos = endPos
					break
				else:
					print("Invalid Move. Please enter a new move.")				
			except:
				print("Please enter your move in the format: A1, A2")
	
	def getMove(self):
		return (self.initPos, self.endPos)
		
	def validateMove(self, position):
		try:
			alpha, number = list(position)
			
			alpha = ord(alpha.upper())
			number = int(number)
			
			## Check if letter is in A-G. Check if number is between 1,8.
			if (73 > alpha > 64) and (0 < number < 9):
				return True		
		except:
			print("Invalid move.")
		return False
