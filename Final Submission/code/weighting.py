from __future__ import division
import math

# makes no change to weight
class static(object):
	def alter(self, current):
		return current
	default = (0,)

# more popular moves are recommended
class popularity(object):

	# iterates popularity by one
	def alter(self, current):
		pop = current[0]
		return (pop + 1,)
	default = (1,)

# moves made by player with highest elo recommended
class elo(object):
	def __init__(self, elo):
		if int(elo) == 0:
			elo = 2000
		self.elo = int(elo)
		self.default = (self.elo,)

    # overrides with higher elo
	def alter(self, current):
		rating = current[0]
		if self.elo > rating:
			return (self.elo,)
		else: return current

# moves with highest win/loss ratio recommended
class winloss(object):
	def __init__(self, new):
		self.new = new 

		# tie
		if self.new == "t":
			self.default = (1,1,1)
		# win
		elif self.new == "w":
			self.default = (2,2,1)
		# loss
		else:
			self.default = (0,0,1)

	def alter(self, current):
		# when backtracking across new moves
		if current == (0,):
			# tie
			if self.new == "t":
				return (1,1,1)
			# win
			elif self.new == "w":
				return (2,2,1)
			# loss
			else:
				return (0,0,1)
		else:
			(weight, win, loss) = current

			#tie
			if self.new == "t":
				return current
			# win
			elif self.new == "w":
				win += 1
				return ((win/loss),win,loss)
			# loss
			else:
				loss += 1
				return ((win/loss),win,loss)

# proprietary lightblue algorithm for weighting
class lightblue(object):
	def __init__(self, elo, wlt):
		if int(elo) == 0:
			elo = 2000
		self.elo = elo
		self.wlt = wlt 

		# tie
		if self.wlt == "t":
			self.default = (math.exp(int(self.elo)/1000)/10,)
		# win
		elif self.wlt == "w":
			self.default = (math.exp(int(self.elo)/1000),)
		# loss
		else:
			self.default = (-1/(math.exp(int(self.elo)/1000)),)

	def alter(self, current):
		value = current[0]
		change = self.default[0]
		return (value + change,)
		


