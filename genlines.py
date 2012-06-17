"""
The purpose of this class is to take in a line (column or row) of
the scrabble board (format: ...foo....) and a tray of letters and
returns all possible valid lines that could be generated with the
tray of letters

examples:
line   : ...cat...
tray   : s
result : (...cat..., ...cats..)

line   : ..rid....
tray   : adled
result : (..rid...., .arid...., ..riddle.)
"""
import os
import re

import linesplit 

def _get_candidate_words(line, tray):
    regex = '^' + line.replace('.', '[%s]?' % tray) + '$'
    command = 'egrep "%s" /usr/share/dict/words' % regex
    words = (word.strip() for word in os.popen(command))
    return words

def _is_line_candidate(line, tray, newline):
    # check if it matches the original line
    regex = '^' + line.replace('.', '[%s.]' % tray) + '$'
    if not re.match(regex, newline):
        return False

    # ensure that it isn't re-using letters in our tray 
    letters = list(line.replace('.', '') + tray)

    for letter in newline.replace('.', ''):
        if not letter in letters:
            return False
        letters.remove(letter)
    
    return True
     
def _get_candidate_lines(line, tray, words):
    for word in words:
        for i in range(len(line) - len(word) + 1):
            newline = '.' * i + word + '.' * (len(line) - len(word) - i)
            if _is_line_candidate(line, tray, newline):
                yield newline

def _genlines(line, tray):
    words = _get_candidate_words(line, tray)
    return _get_candidate_lines(line, tray, words)

def genlines(line, tray):
    for lhs, mid, rhs in linesplit.split(line):
        for x in _genlines(mid, tray):
            yield lhs + x + rhs
    
if __name__ == '__main__':
    line = '..hong..kong..phoey..'
    tray = 'tileu'
    print list(genlines(line, tray) )
     

