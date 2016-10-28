def isBonito(num):
    bonito = (num * 3) + 11
    aux = 0
    for i in range(len(str(bonito))):
        print(str(bonito)[i])
        aux += int(str(bonito)[i])
    if (aux == num):
        return True
    else:
        return False

print(isBonito(8))
print(isBonito(9))