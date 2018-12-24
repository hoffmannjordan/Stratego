import numpy as np
import matplotlib.pyplot as plt


#pieces = [10,9,8,7,6,5,4,3,2,'S','B','F']
pieces = [10,9,8,7,6,5,4,3,2, 20 , 21 , 22]
counts = [1 ,1,2,3,4,4,5,5,6, 1  , 6  , 1 ]




def gen_random_init_board():
	all_pieces = np.zeros(40)
	j = 0 
	for i in range(len(counts)):
		for k in range(counts[i]):
			all_pieces[j] = pieces[i]
			j += 1
	print all_pieces
	board = np.zeros((10,10))
	board[4:6,2:4] = -1
	board[4:6,6:8] = -1
	
	#plt.spy(board)
	#plt.show()

