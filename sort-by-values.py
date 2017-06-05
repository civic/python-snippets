import operator
d = {"a": 3, "b": 2, "c": 1}

for k in sorted(d, key=d.get):
    print(k, d[k])
