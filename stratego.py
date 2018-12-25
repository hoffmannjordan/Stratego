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
        self.board = board
        self.turn  = turn

    def move(self):
    	print 'here'