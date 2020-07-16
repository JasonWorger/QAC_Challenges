# Making a List
julyDevops = ["Christopher", "John", "Jason", "Arsalan", "Domenico", "Joshua", "Ryan", "Bradley", "Javas", "Sithembiso",
              "Jacob", "Clifford", "Wasim", "Mohamed", "Tobias", "Christopher", "Samuel", "Edmund", "Amanda", "Steven",
              "Jack"];

# Adding Luke to the list
julyDevops.append("Luke")
print(julyDevops)

# Printing the 5th name in the list
print(julyDevops[4])

## Count method 1

# Using the count function for the name Chris in the list
julyDevops.count("Christopher")

print(julyDevops.count("Christopher"))

## Count method 2

#Creating the count variable to print the number of Chris
count = julyDevops.count("Christopher")

# Printing the number of Chris
print("The number of Christopher in cohort is:", count)

