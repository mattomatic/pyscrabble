"""
A class containing the timeit decorator -- use this to time functions
"""
import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r %f sec' % (method.__name__, te - ts)

        return result
    
    return timed 
