# Works with mypy <programename>; https://github.com/python/mypy

# def add(a: int, b: int) -> int:
#     return a + b

# name: str = "ChatGPT"
# age: int = 25
# age2: int = 46

# print(add(age2, age))
# print(add(name, age))


# ------------------------

from typing import List, Dict, Tuple, Optional

def greet_all(names: List[str]) -> None:
    for name in names:
        print(f"Hi {name}")

greet_all(["Ani", "Sam", "Elon", "Bill"])
