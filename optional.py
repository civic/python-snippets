#! ./venv3/bin/python

from typing import Optional


def func() -> Optional[str]:
    return "Hello"

s: Optional[str] = func()

print(s+"aa")
