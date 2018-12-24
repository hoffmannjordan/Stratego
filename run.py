import numpy as np
from stratego import *
from gen_board import *
if __name__=='__main__':
	gen_random_init_board()
	stratego = Stratego(1,1)
	stratego.setup()