
def callLimit(limit: int):
    if not (isinstance(limit, int)):
        return("limit must be an int")
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            try:
                nonlocal count
                if count >= limit:
                    raise AssertionError(f"Error: {function} call too many times")
                else:
                    count +=1
                    function(*args, **kwds)
            except AssertionError as e:
                print(e)
        return limit_function
    return callLimiter


@callLimit(3)
def f():
    print ("f()")

@callLimit(1)
def g():
    print ("g()")

for i in range(3):
    f()
    g()
