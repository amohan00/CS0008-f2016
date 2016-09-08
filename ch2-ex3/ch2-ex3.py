# asks the user to enter land in square meters and calculates the number of acres

# here I am asking the user to input a value for the area of their land and assigning that number to a variable.
land = float(input("Enter area of land in square meters. Please use only numbers and decimals: "));
# here I am reassiging the variable to the user's input divided by one acre to find how many acres it is equal to.
land = land/4046.8564224;
# here I am printing the total number of acres
print ("There are ", land, " acres in this tract");