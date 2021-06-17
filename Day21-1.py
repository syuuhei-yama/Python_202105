import time

def memoize(f):
    cache = {}
    def _wrapper(n):
        if n not in cache:
            cache[n] = f(n)
        # print("befor")
        # r = f(n)
        # print("after")
        return cache[n]
    return _wrapper

# @memoize
# def test(n):
#     print("test")
#
# print(test(10))

@memoize
def long_func(num : int) -> int:
    r = 0
    for i in range(10000000):
        r += num + 1
    return r


if __name__ == "__main__":
    for i in range(10):
        print(long_func(i))

    start = time.time()
    for i in range(10):
        print(long_func(i))
    print(time.time() - start)

