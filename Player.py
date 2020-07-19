class Player:
	
	def __init__(self, player):
		self.Name = input("Enter your name: ")
		self.player = player

	def getMove(self):
		
		while True:
			move = input("Enter your move: ")
			try:
				initPos, endPos = move.split(', ')
				print(initPos, endPos)
				break;
			except:
				print("Please enter your move in the format: A1, A2")
		print("Works")

		
		
		print("Initialising Player 1")		
p1 = Player("White")
p1.getMove()