def foo():
    import math
    s = "foobar"
    letter = "o"
    return math.floor(s.count(letter) / len(s) * 100)


print(foo())

