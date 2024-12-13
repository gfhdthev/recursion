palin = 'а роза упала на лапу Азора'
palin = palin.lower()
for i in palin:
    if i == ' ': 
        palin = palin[:palin.index(i)] + palin[palin.index(i)+1:]

def palindrom(b: str) -> bool:

    if len(b) == 0:
        return True

    if b[0] != b[-1]:
        return False

    return palindrom(b[1:-1])

res = palindrom(palin)

if res is True:
    print('Строка - палиндром')
else:
    print('Строка - не палиндром')