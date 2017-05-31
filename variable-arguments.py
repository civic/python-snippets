# coding: utf8

# 引数2つ目移行は可変長引数
def func1(a, *others):
    print(a)
    for o in others:
        print(o)

    print("")


print("@@@ variable args")
func1(1)
func1(1, 2)
func1(1, 2, 3)
func1(*[9,8,7]) #listを引数リストに展開



# 引数2つ目移行は可変キーワード引数
def func2(a, **others):
    print(a)
    for k,v in others.items():
        print(k+"="+str(v))

    print("")


print("@@@ variable keyward args")
func2(1)
func2(a=1, b=2, c=3)


# 可変長引数+可変キーワード引数
def func3(*args, **kwargs):
    for a in args:
        print(a)

    for k,v in kwargs.items():
        print(k+"="+str(v))

    print("")


print("@@@ variable list and keyward args")
func3(1, 2, foo=3, bar=4)


