class Player:
	
	def __init__(self, player):
		self.Name = input("Enter your name: ")
		self.player = player

	def setMove(self):
		while True:
			move = input("Enter your move: ")		
			try:
				initPos, endPos = move.split(', ')
				if self.validateMove(initPos) and self.validateMove(endPos):
					self.initPos = initPos
					self.endPos = endPos
					break;
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
			if (alpha < 72 and alpha > 64) and (number > 0 and number < 9):
				return True		
		except:
			print("Invalid move.")
		return False
		 

	
print("Initialising Player 1")		
p1 = Player("White")
p1.setMove()
print(p1.getMove())