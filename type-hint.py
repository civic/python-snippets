#! venv3/bin/python
import sys

print(sys.version)
def concat(s:str, n:str)->str:
    return s + n

concat("Hello", "World")    # "HelloWorld"
#concat(1, 2)

#concat("s", 2)              # TypeError: must be str not int

from typing import List

a:List[str] = []

a.append("hello")
a.append(1) # ! Argument 1 to "append" of "list" has incompatible type "int"; expected "str"


from typing import TypeVar, Generic

T = TypeVar('T')
class MyContainer(Generic[T]):
    def set(self, v:T):
        self.value:T = v
    def get(self) -> T:
        return self.value

container = MyContainer[int]()
container.set(1)
container.get() + 3

container.set("Hello")     # ! Argument 1 to "set" of "MyContainer" has incompatible type "str"; expected "int" 
container.get().index("l")  # ! "int" has no attribute "index"
