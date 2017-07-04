import itertools

r1 = range(0, 3)
r2 = range(3, 6)

stream = (r1, r2)
print(stream)


flat = itertools.chain(r1, r2)
for n in flat:
    print(n)

flat2 = itertools.chain.from_iterable(stream)
for n in flat2:
    print(n)



