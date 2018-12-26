import numpy as np
from stratego import *
from gen_board import *


if __name__=='__main__':
	board,legal_board =  gen_random_init_board()
	board_1, board_2  = np.clip(board,0,100),np.clip(-board,0,100)
	print board_1
	stratego          = Stratego(board_1,board_2,0)
	stratego.gen_moves()
	print 'here'
	exit()
	stratego.setup()

	stratego.play()