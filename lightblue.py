''' main application '''

import parser
import chess as ch
import graph
import weighting
import sys

# intro 
print "Welcome to Light Blue!"
print "Type quit at any time to quit the application."
print "Instructions:" 
print "Type in the move each player makes in Standard Algebraic Notation (SAN)"
print "  (a) For pawns, type the piece's origin coordinate, \
a dash, then the final coordinate"
print "       example: tying 'e2-e4' (without quotes) \
moves a pawn from e2 to e4"
print "  (b) For pieces other than pawns, first type the first letter \
of the piece's name in upper-case"
print "      followed by the pawn notation."
print "      example: typing 'Qd1-f3' (without quotes) \
moves the queen from d1 to f3"
print "      NOTE: the letter for knight is 'N' not 'K' because \
'K' is already used to denote the Kings"
print "  (c) For moves where pieces are captured, the dash \
should be changed to lower-case 'x'"
print "      example: typing 'Qf3xf7' (without quotes) moves \
the queen from f3 and captures a piece at f7"
print "  (d) Denote castling with upper-case letter O's separated by dashes"
print "      (i) 'O-O' queenside"
print "      (ii) 'O-O-O' kingside"
print "  (e) Moves are denoted the same way, \
regardless of the side making the move."
print "      The program automatically tracks which side \
should be moving, allowing it to correctly"
print "      interpret which piece to move."
print "  (f) Illegal moves will be cause the program \
to terminate with exceptions due to"
print "      code from the chess API that light_blue uses."
print "  (g) Please see http://en.wikipedia.org/wiki/Rules_of_chess \
for the complete set of chess rules."

# grab white elo and check if positive int
whiteelo = raw_input("What is the White player's elo rating? (type 0 if unsure) ")
if whiteelo == "42":
        print "Functions are values."
while not whiteelo.isdigit():
        if whiteelo == "quit":
                sys.exit()
	print "Elo must be a positive integer."
        whiteelo = raw_input("What is the White player's elo rating? (type 0 if unsure) ")

# grab black elo and check if positive int
blackelo = raw_input("What is the Black player's elo rating? (type 0 if unsure) ")
if blackelo == "42":
        print "Functions are values."
while not blackelo.isdigit():
        if blackelo == "quit":
                sys.exit()
	print "Elo must be a positive integer."
        blackelo = raw_input("What is the Black player's elo rating? (type 0 if unsure) ")
print "Available weighting algorithms include:"
print "\"lightblue\""
print "\"pop\""
print "\"elo\""
print "\"wl\""
print "\"static\""
weight_type = raw_input("What kind of weighting would you like to use? ")
while weight_type != "lightblue" \
      and weight_type != "pop" \
      and weight_type != "elo" \
      and weight_type != "wl" \
      and weight_type != "static":
        if weight_type == "quit":
                sys.exit()
        print "Must choose valid weighting algorithm."
        weight_type = raw_input("What kind of weighting would you like to use? ")

# prompts user to wait
print "Loading... please wait"

# check and checkmate/stalemate verification
check_message = "You're in check!"
def stalemate():
	#print "Stalemate broken"
	side = current_game.board.get_turn()
	return ch.Board.is_stalemate(current_game.board, side)
def checkmate(): 
	side = current_game.board.get_turn()
	return ch.Board.is_mate(current_game.board, side)
def check():
	side = current_game.board.get_turn()
	return ch.Board.is_check(current_game.board, side)
def checkmate_fun(color, weight_type, mvlst):
	# corrects color again
	if color == 'w':
		print "Checkmate! White Wins!"
		winnerelo = whiteelo
		loserelo = blackelo
	else:
		print "Checkmate! Black Wins!"
		winnerelo = blackelo
		loserelo = whiteelo
	print "Congrats and thanks for using Light Blue."
	print "Made by Phillip Huang, Collin Styring, Javier Cuan-Martinez and Chris Chen for CS51."

	# backtracking
	if weight_type == "wl":
		# generates new weight_objs
		winner_obj = weighting.winloss('w')
		loser_obj = weighting.winloss('l')

		for (a,b,c,d,e) in mvlst:
			if d == color:
				graph.recommend(winner_obj,b,c,d,e)
			else:
				graph.recommend(loser_obj,b,c,d,e)

	elif weight_type == "lightblue":
		# generates new weight_objs
		winner_obj = weighting.lightblue(winnerelo, 'w')
		loser_obj = weighting.lightblue(loserelo, 'l')

		for (a,b,c,d,e) in mvlst:
			if d == color:
				graph.recommend(winner_obj,b,c,d,e)
			else:
				graph.recommend(loser_obj,b,c,d,e)
def stalemate_fun(weight_type, mvlst):
	print "The game is at a draw!"
	print "Congrats and thanks for using Light Blue."
	print "Made by Phillip Huang, Collin Styring, Javier Cuan-Martinez and Chris Chen for CS51."

	# backtracking
	if weight_type == "wl":
		# generates new weight_objs
		weight_obj = weighting.winloss('t')
		# backtracks
		for (a,b,c,d,e) in mvlst:
				graph.recommend(weight_obj,b,c,d,e)

	elif weight_type == "lightblue":
		# generates new weight_objs
		winner_obj = weighting.lightblue(winnerelo, 't')
		loser_obj = weighting.lightblue(loserelo, 't')

		for (a,b,c,d,e) in mvlst:
			if d == color:
				graph.recommend(winner_obj,b,c,d,e)
			else:
				graph.recommend(loser_obj,b,c,d,e)

# selects weighting object
if weight_type == "pop":
    weight_obj = weighting.popularity()
elif weight_type == "elo":
    weight_objw = weighting.elo(whiteelo)
    weight_objb = weighting.elo(blackelo)
elif weight_type == "wl":
    weight_obj = weighting.static()
elif weight_type == "lightblue":
    weight_obj = weighting.static()
elif weight_type == "static":
    weight_obj = weighting.static()
else: 
    raise "invalid weight type"
mvlst = []

# loads graph
graph.initialize()
graph.load("Carlsen" + weight_type)

# initializes board
current_game = ch.Game()
current_game.setup()
color = 'w'
quit = False

# prints starting position
print "Here is the board:"
print current_game.board

# first recommend
lst = graph.firstrecommend()
lstlen = len(lst)
if lstlen == 1:
	(x,y) = lst[0]
	print "You should make this move:", x
	print "It should give you:"
	print y
elif lstlen == 0:
	print "Error: No Data"
	quit = True
else:
	print "You should make one of these moves:"
	for item in lst:
		(x,y) = item
		print "One possible move is:", x
		print "It should give you:"
		print y

# recommending moves
while quit == False:

	if color == 'w':
		print "White's Turn"
	else: 
		print "Black's Turn"

	# checks for quit and help
	mv = raw_input("What is your move? ")
	if mv == "quit":
		print "Unloading files... please wait"
		break
	
	# makes move and grabs configs
	before = str(current_game.board)
	current_game.board.move(mv)
	after = str(current_game.board)

	# prints current board
	print "\n\n\n\n\n\n\n"
	print "---------------------"
	print "Here is the board:"
	print after

	# win loss backtrack storage
	if weight_type == "wl" or weight_type == "lightblue":
		mvlst.append((weight_obj,before,mv,color,after))

	# generate recommendation
	if weight_type == "elo":
		if color == 'w':
			lst2 = graph.recommend(weight_objw,before,mv,color,after)
		else: 
			lst2 = graph.recommend(weight_objb,before,mv,color,after)
	else:
		lst2 = graph.recommend(weight_obj,before,mv,color,after)
	lst2len = len(lst2)
	if lst2len == 1:
		if stalemate():
			stalemate_fun(weight_type, mvlst)
			break 
		if checkmate():
			checkmate_fun(color, weight_type, mvlst)
			break
		if check():
			print check_message
		(x,y) = lst2[0]
		print "You should make this move:", x
		print "It should give you:"
		print y
	elif lst2len == 0:
		if stalemate():
			stalemate_fun(weight_type, mvlst)
			break 
		if checkmate():
			checkmate_fun(color, weight_type, mvlst)
			break
		if check():
			print check_message
		print "No Data: Make a random move"
	else:
		if stalemate():
			stalemate_fun(weight_type, mvlst)
			break 
		if checkmate():
			checkmate_fun(color, weight_type, mvlst)
			break
		if check():
			print check_message
		print "You should make one of these moves:"
		for item in lst2:
			(x,y) = item
			print "One possible move is:", x
			print "It should give you:"
			print y

	# color correction
	if color == 'w':
		color = 'b'
	else: 
		color = 'w'

graph.save("Carlsen" + weight_type)
