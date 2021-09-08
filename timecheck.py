import time

def time_checker(func) :
    #Free variable
    def perf_clocked(*args) :
        # function start time
        st = time.perf_counter()
        # function run
        result = func(*args)
        # function end time
        et = time.perf_counter() - st
        # function name
        name = func.__name__
        # function variable
        arg_str = ', '.join(repr(arg) for arg in args)
        # print result
        print('[%0.5fs %s(%s) -> %r' % (et,name,arg_str,result))
        return result
    return perf_clocked 