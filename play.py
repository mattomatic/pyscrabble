import random
import time
import numpy as np

import genboards

read_file = lambda x: np.array([list(row.strip()) for row in open('boards/test1.txt')])

if __name__ == '__main__':
    board = read_file('boards/test1.txt')
    tray = 'saecatsnr'

    while True:
        boards = []
        start = time.time()
        for newboard in genboards.genboards(board, tray):
            boards.append(newboard)
        

        print 'round summary'
        print '%d boards created' % len(boards)
        print 'start board'
        print board

        board = boards[random.randint(0, len(boards))]

        print 'end board'
        print board

        print 'time'
        print time.time() - start


