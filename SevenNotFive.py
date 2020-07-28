def sevennotfive(start,end):
    numbersbyseven= []
    for x in range(start, end):
        if (x%7==0) and (x%5!=0):
            numbersbyseven.append(str(x))
    return ','.join(numbersbyseven)

print(sevennotfive(2000,3201))
