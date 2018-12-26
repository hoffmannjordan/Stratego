import numpy as np
from stratego import *
from gen_board import *

def modify_board():


if __name__=='__main__':
	board,legal_board =  gen_random_init_board()
	board_1, board_2  = np.clip(board,0,100),np.clip(-board,0,100)
	print board_1
	exit()
	stratego          = Stratego(1,1)
	stratego.setup()