import numpy as np

#pieces = [10,9,8,7,6,5,4,3,2,'S','B','F']
pieces = [10,9,8,7,6,5,4,3,2, 20 , 21 , 22]
counts = [1 ,1,2,3,4,4,4,5,8, 1  , 6  , 1 ]

# 21 can not move
# 22 can not move
# 2 can move as far in any direction
class Stratego():
    def __init__(self, board1, board2, turn):
        """Initialization"""
        self.board1 = board1
        self.board2 = board2

        self.turn  = turn

    def move(self):
    	if turn == 0:
    		board = self.board1
    	else:
    		board = self.board2

    	pieces = np.where(board > 0)

    	moves = []

    	for i in range(len(pieces)):
    		'''player 1 moves from high numbers down'''
    		'''player 2 moves from low numbers up'''