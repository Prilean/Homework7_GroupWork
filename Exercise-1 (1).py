from typing import Iterable


def replace_first(items: list) -> Iterable:
    
    return items[-1:len(items):] + items[:-1]


if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([2, 3, 4, 1])))