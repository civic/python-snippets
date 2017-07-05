#! venv3/bin/python


def concat(s:str, n:str)->str:
    return s + n

concat("Hello", "World")    # "HelloWorld"
concat(1, 2)

concat("s", 2)              # TypeError: must be str not int

