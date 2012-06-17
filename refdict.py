"""
a reference dictionary class
"""
import re

values = {'a': 1, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2, 'f': 4, 'i': 1, 'h': 4, 'k': 5, 'j': 8, 'm': 3, 'l': 1, 'o': 1, 'n': 1, 'q': 10, 'p': 3, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 4, 'x': 8, 'z': 10}

def prefix_exists(prefix):
    try:
        return reduce(lambda node, letter: node[letter], prefix, tree)
    except:
        return None

def word_exists(word):
    return prefix_exists(word + '*')

def get_value(word):
    return sum([values[letter] for letter in word])

def _get_tree(words):
    root = {}
    node = root
    for word in words:
        node = root
        for letter in word:
            if not letter in node:
                node[letter] = {}
            node = node[letter]
        node['*'] = get_value(word)
    return root

wfile = '/usr/share/dict/words'
words = [word.strip() for word in open(wfile) if re.match('[a-z]+', word)]
tree  = _get_tree(words)

if __name__ == '__main__':
    print word_exists('apple')
    print word_exists('pear')
