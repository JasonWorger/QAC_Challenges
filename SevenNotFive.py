def sevennotfive(start,end):
    numbersbyseven= []
    for x in range(start, end):
        if (x%7==0) and (x%5!=0):
            numbersbyseven.append(x)
    return numbersbyseven

print(sevennotfive(2000,3200))
