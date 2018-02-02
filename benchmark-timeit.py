import timeit

def number_join_by_forloop():
    s = "-"
    for n in range(10000):
        s += str(n)
    return s


def number_join_by_mapjoin():
    return "-".join(map(str, list(range(10000))))

t1 = timeit.timeit('number_join_by_forloop()', number=1000, globals=globals())
print("for loop: %.3f sec" % t1)


t2 = timeit.timeit('number_join_by_mapjoin()', number=1000, globals=globals())
print("map join: %.3f sec" % t2)

t2 = timeit.timeit('from __main__ import number_join_by_mapjoin; number_join_by_mapjoin()', number=1000)
print("map join: %.3f sec" % t2)
