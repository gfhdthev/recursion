find_sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sum(b: list) -> int:
    if len(b) == 0:
        return 0
    return b[0] + sum(b[1:])

print(sum(find_sum))