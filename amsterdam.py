def amsterdam(input): 
    input = input.lower()
    split_by_spaces = input.split()
    count = 0
    for i in split_by_spaces:
        if i == "am": 
            count += 1
    return count

print(amsterdam("Am I in Amsterdam"))
print(amsterdam("I am in Amsterdam am I"))
print(amsterdam("I have been in Amsterdam"))