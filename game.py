class Board:
	def __init__(self):
		self.board = [4] * 6 + [0] + [4] * 6 + [0]

	def turn(self, player, position):
		assert (player == 0 or player == 1), "Not a valid position"
		assert (position >= 0 and position <= 5 and type(position) is int), "Not a valid position"
		# calculate starting position
		curr = player * 7 + position
		amount = self.board[curr]
		if (amount == 0):
			print("You picked an empty space! You will have to pick again.")
			return player

		self.board[curr] = 0
		while (amount > 0):
			curr = (curr + 1) % len(self.board)
			if ((curr != 6 and player == 1) or (curr != 13 and player == 0)):
				self.board[curr] += 1
				amount -= 1
		if ((player == 0 and curr == 6) or (player == 1 and curr == 13)):
			return player
		elif (self.board[curr] == 1):
			correctRange = (player == 0 and curr in range(6)) or (player == 1 and curr in range(7, 13))
			if (correctRange):
				print("Player " + str(player) + " successfully stole some pieces!")
				opp = 12 - curr
				stole = self.board[opp]
				self.board[opp] = 0
				stole += self.board[curr]
				self.board[curr] = 0
				if player == 0:
					self.board[6] += stole
				else:
					self.board[13] += stole
		return 1 - player

	def isTerminal(self, player):
		if (player == 0):
			for i in range(6):
				if (self.board[i] != 0):
					return False
		else:
			for i in range(7, 13):
				if (self.board[i] != 0):
					return False
		print("Player " + str(player) + " ran out of moves.")
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
		if (total1 > total2):
			print("Player 0 Won! " + str(total1) + " to " + str(total2) + ".")
		elif (total1 < total2):
			print("Player 1 Won! " + str(total2) + " to " + str(total1) + ".")
		else:
			print("Tie! " + str(total2) + " to " + str(total1) + ".")


	def getState(self):
		print("\n")
		print("*" * 24)
		print("---" + str(list(range(6))[::-1]) + "---\n")
		print(str(self.board[::-1][:7]))
		print("---" + str(self.board[:7]))
		print("\n---" + str(list(range(6))) + "---")
		print("*" * 24)
		print("\n")

def main():
	board = Board()
	currPlayer = 0
	while not board.isTerminal(currPlayer):
		board.getState()
		position = int(input("Which position does player " + str(currPlayer) + " want? "))
		currPlayer = board.turn(currPlayer, position)
	board.cleanUp()
	board.getState()

main()


