"""
This class takes a line in our format '...foo...bar...' and 
splits it into all combinations of adjacent groupings. 

examples:
foo.bar           -> (foo., .bar, foo.bar)
..foo..bar..biz.. -> (..foo.., ..bar.., ..biz..,
                      ..foo..bar.., ..bar..biz..,
                      ..foo..bar..biz..)
"""
import itertools
import re

def _grouper(iter, n):
    for offset in range(n):
        for index, item in enumerate(iter):
            if index+offset+1 <= len(iter):
                yield iter[index:index+offset+1]

def _shave(lhs, mid, rhs):
    """
    Shave off the leading and trailing .'s of words that are 
    adjacent to other words. This is so that the word finder
    doesn't create words that run together.

    examples:
    (..raj, ..dar.., bar..) -> (..raj., .dar., .bar..)
    """
    if lhs:
        assert mid[0] == '.'
        lhs = lhs + '.'
        mid = mid[1:]

    if rhs:
        assert mid[-1] == '.'
        mid = mid[:-1]
        rhs = '.' + rhs

    return (lhs, mid, rhs)

def split(text):
    """
    Split the text (format: ...bar..foo) into combinations
    of adjacent groupings
    """
    groups = list(re.finditer('[.]*[^.]+', text))
    groupings = _grouper(groups, len(groups))

    for grouping in groupings:
        lhs = grouping[0]
        rhs = grouping[-1]

        lhs_text = text[:lhs.start()]
        grp_text = text[lhs.start():rhs.end()]
        rhs_text = text[rhs.end():]

        # Now -- add the trailing ...'s to the grp
        grp = re.match('^[.]+', rhs_text)

        if grp:
            grp_text = grp_text + rhs_text[grp.start():grp.end()]
            rhs_text = rhs_text[grp.end():]
        
        lhs_text, grp_text, rhs_text = _shave(lhs_text, grp_text, rhs_text)

        yield (lhs_text, grp_text, rhs_text)

if __name__ == '__main__':
    print list(linesplit('..hong..kong..phoey..'))
