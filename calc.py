def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a, bは数値である必要があります")
    return a + b


def subtract(a, b):
    #リモート側での変更
    return a - b

def multiply(a, b):
    return a * b
