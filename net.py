import numpy as np

#pieces = [10,9,8,7,6,5,4,3,2,'S','B','F']
pieces = [10,9,8,7,6,5,4,3,2, 20 , 21 , 22]
counts = [1 ,1,2,3,4,4,4,5,8, 1  , 6  , 1 ]

# 21 can not move
# 22 can not move
# 2 can move as far in any direction
class Stratego():
    def __init__(self, board1, board2, board3, board4, turn):
        """Initialization"""
        self.board1 = board1
        self.board2 = board2

		self.board3 = board3 #what player one knows in board 2
        self.board4 = board4 #what player two knows in board 1

        self.turn  = turn

    def gen_moves(self):