import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#pieces = [10,9,8,7,6,5,4,3,2,'S','B','F']
pieces = [10,9,8,7,6,5,4,3,2, 20 , 21 , 22]
counts = [1 ,1,2,3,4,4,4,5,8, 1  , 6  , 1 ]




def gen_random_init_board():
	all_pieces = np.zeros(40)
	j = 0 
	for i in range(len(counts)):
		for k in range(counts[i]):
			all_pieces[j] = pieces[i]
			j += 1

	board = np.zeros((10,10))
	board[4:6,2:4] = -1
	board[4:6,6:8] = -1
	to_put_1 = np.random.permutation(all_pieces)	
	i = 0
	j = 0
	for k in range(len(to_put_1)):
		board[i,j] = to_put_1[k]
		j += 1
		if j == 10:
			j = 0
			i += 1
	to_put_1 = np.random.permutation(all_pieces)	
	i = 6
	j = 0
	for k in range(len(to_put_1)):
		board[i,j] = - to_put_1[k]
		j += 1
		if j == 10:
			j = 0
			i += 1
	return board
	# sns.heatmap(board, cmap =sns.palplot(sns.color_palette("hls", 8)))
	# plt.show()

