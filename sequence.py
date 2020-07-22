def sorted_list(input):
    myList = input.split()
    mySet = set(myList)
    mySort = sorted(mySet, key=str.casefold)
    myString = " ".join(mySort)
    return myString
