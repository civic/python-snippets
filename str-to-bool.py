from distutils.util import strtobool 

for s in ["false", "true", "T", "1", "F", "0", "TRUE"]:
    b1 = s.lower() in ["t", "true", "T", "1"]
    b2 = strtobool(s)
    print("%s ==> %s, %s" % (s, bool(b1), bool(b2)))

