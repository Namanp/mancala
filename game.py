class Board:

	def __init__(self):
		self.board = [4] * 6 + [0] + [4] * 6 + [0]

	def turn(self, player, position):
		assert (player == 0 or player == 1), "Not a valid position"
		assert (position >= 0 and position <= 5 and type(position) is int), "Not a valid position"
		# calculate starting position
		curr = player * 7 + position
		amount = self.board[curr]
		board[curr] = 0
		curr += 1
		while (amount > 0):
			if ((curr != 6 and player == 1) or (curr != 13 and player == 0)):
				self.board[curr] += 1
				amount -= 1
				if (amount == 0 and self.board[curr] == 1):
					opp = 12 - curr
					stole = self.board[opp]
					self.board[opp] = 0
					self.board[curr] += stole

			curr = (curr + 1) % len(self.board)

	def isTerminal(self, player):
		if (player == 0):
			for i in range(6):
				if (self.board[i] != 0):
					return False
		else:
			for i in range(7, 13):
				if (self.board[i] != 0):
					return False
		return True

	def cleanUp(self):
		total1 = 0
		for i in range(6):
			total1 += self.board[i]
			self.board[i] = 0
		total2 = 0
		for i in range(7, 13):
			total2 += self.board[i]
			self.board[i] = 0
		self.board[6] += total1
		self.board[13] += total2

	def getState(self):
		print("\n")
		print("*" * 24)
		print(str(self.board[::-1][:7]))
		print("---" + str(self.board[:7]))
		print("*" * 24)
		print("\n")

board = Board()
board.getState()
board.turn(0, )


