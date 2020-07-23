def Value(n):
    number_1 = int( "%s" % (n) )
    number_2 = int( "%s%s" % (n,n) )
    number_3 = int( "%s%s%s" % (n,n,n) )
    number_4 = int( "%s%s%s%s" % (n,n,n,n) )
    total = (number_1+number_2+number_3+number_4)
    return total