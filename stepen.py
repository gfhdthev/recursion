def stepen(a: int, b: int) -> int:
    if b == 0:
        return 1
    return a * stepen(a, b-1)

print(stepen(2, 20))