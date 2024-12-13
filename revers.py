rev = 'а роза упала на лапу Азора'

def revers(b: str) -> str:
    if len(b) == 0:
        return b
    return revers(b[1:]) + b[0]

res = revers(rev)

print(res)