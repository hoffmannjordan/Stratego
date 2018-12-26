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
    	'''
    	Function that generates all possible next boards.
    	Returns all the available boards in the next position
    	'''
    	if self.turn == 0:
    		board = self.board1
    	else:
    		board = self.board2

    	pieces = np.where(board > 0)
    	moves = []
    	print 'k'
    	for i in range(len(pieces[0])):
    		me = board[pieces[0][i],pieces[1][i]]
    		if me != 21 and me != 22:
    			if me == 20: # SPY
    				'''
    				Can reveal one in opponents board
    				'''
    			elif me = 2:
    				'''
    				Can move arbitrarily far in any direction
    				'''
    			else:
    				'''
    				can only move one square in any direction
    				'''
    		'''player 1 moves from high numbers down'''
    		'''player 2 moves from low numbers up'''

    def MCTS(self,net1,net2):
    	'''
    	Function that takes in the previous boards and samples them based on net function with win probabiltiy.
    	Choose options based on that win probability.
    	Rollout to the end of the game.
    	Make sure to store things to determine who won
    	'''

    def play(self):
    	'''
    	Play the game by rolling out. Store things.
    	'''