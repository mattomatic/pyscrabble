"""
This class generates all valid new boards given a tray of letters
and an input board. 

arguments:
  board -- a matrix of letters
  tray -- a tray of letters, eg abjeijflk
"""
import multiprocessing
import genlines 
import re

import refdict

def _validate_line(line):
    """
    Make sure that everything in this line is a word -- we do this
    by grepping the dictionary and ensuring that each word appears
    exactly one time
    """
    words = re.findall('[^.][^.]+', line)
    
    if not words:
        return True

    for word in words:
        if not refdict.word_exists(word):
            return False
    
    return True

def _validate_cols(board):
    for i in range(board.shape[1]):
        if not _validate_line(''.join(board[:, i])):
            return False
    return True

def _validate_rows(board):
    for i in range(board.shape[0]):
        if not _validate_line(''.join(board[i, :])):
            return False
    return True

def _genboards_row(board, tray, linenum):
    newboards = []

    line = ''.join(board[linenum,:])
    newlines = genlines.genlines(line, tray)

    for newline in newlines:
        newboard = board.copy()
        newboard[linenum,:] = list(newline)
        if _validate_cols(newboard):
            newboards.append(newboard)
    return newboards

def _genboards_col(board, tray, linenum):
    newboards = []

    line = ''.join(board[:,linenum])
    newlines = genlines.genlines(line, tray)

    for newline in newlines:
        newboard = board.copy()
        newboard[:,linenum] = list(newline)
        if _validate_rows(newboard):
            newboards.append(newboard)
    return newboards

def _genboards(x):
    board, tray, is_row, linenum = x
    
    if is_row:
        return _genboards_row(board, tray, linenum)
    else:
        return _genboards_col(board, tray, linenum) 

def genboards(board, tray):
    args = []

    for rownum in range(board.shape[0]):
        args.append((board, tray, True, rownum))

    for colnum in range(board.shape[1]):
        args.append((board, tray, False, colnum))
   
    results = []
    map(results.extend, pool.map(_genboards, args))
    return results

pool = multiprocessing.Pool(processes=4)
