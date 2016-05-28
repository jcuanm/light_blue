''' parses through large amounts of single-game PGNs
    and imports data into graph '''

import chess as ch
import copy
import glob
import graph
import weighting
import sys
import reg_exp

'''
At the moment, this code prints out one game in this format:
Old Board Configuration
Move that was made
Player Color who just moved
New Board Configuration
'''

        
# parses and imports through individual-game PGNs 
def main():

    # keeping track of file progress
    count = 0

    # saves user choice of weighting algorithm
    weight_type = sys.argv[1]

    # sets up graph
    graph.initialize()

    # for each pgn file
    for f in glob.iglob('*.pgn'):

        # initializes games
        game = ch.Game()
        new_game = ch.Game()
        new_game.setup()
        piece_color = ""

        # opens and imports file into game
        pgn_file = open(f, 'r')
        pgn = game.import_pgn(pgn_file)

        # elo and win/loss parsing
        reg_result = reg_exp.reg_exp(f)

        # for each move
        for move in game.moves:

            # grabs configuration before the move
            old_board = new_game.board
            old_board_copy = copy.deepcopy(old_board)

            # makes move
            new_game.move(move)

            # grabs configuration after the move
            new_board = new_game.board
            new_board_copy = copy.deepcopy(new_board)

            # elo and win/loss formatting
            if new_game.board.get_turn() == 0:
                piece_color = "b"
                elo = reg_result[1]
                if reg_result[2] == "black":
                    wlt = 'w'
                elif reg_result[2] == "white":
                    wlt = 'l'
                else:
                    wlt = 't'  
            else:
                piece_color = "w"
                elo = reg_result[0]
                if reg_result[2] == "black":
                    wlt = 'l'
                elif reg_result[2] == "white":
                    wlt = 'w'
                else:
                    wlt = 't'

            # selects weighting object
            if weight_type == "pop":
                weight_obj = weighting.popularity()
            elif weight_type == "elo":
                weight_obj = weighting.elo(elo)
            elif weight_type == "wl":
                weight_obj = weighting.winloss(wlt)
            elif weight_type == "lightblue":
                weight_obj = weighting.lightblue(elo, wlt)
            elif weight_type == "static":
                weight_obj = weighting.static()
            else: 
                raise "Usage: python parser.py weight_type"

            # imports into graph
            graph.recommend(
                weight_obj, 
                str(old_board_copy), 
                str(move), 
                piece_color, 
                str(new_board_copy))

        # close file
        pgn_file.close()

        # keeps track of progress
        count += 1
        print count
        print f


    ''' change here '''
    # saves graph to file
    graph.save("Carlsen100" + weight_type)


    ''' change here '''
    # DEBUGGING: prints weights 
    for x in graph.graph:
        for y in graph.graph[x]:
            print graph.graph[x][y][1]


if __name__ == '__main__':
	main()
