#practice program in class

number = input("Give me a number: ");
number = int(number);
if (number < 0 or number > 36):
    print ("Give me a number!!")
else:
    if (number == 0):
        color = "Green"
    elif (number > 0 and number <= 10)\
    or\
    (number > 19 and number <= 28):
        if (number%2 == 0):
            color = "Black"
        else:
            color = "Red"
    elif (number > 10 and number <= 18):
        if (number%2 == 0):
            color = "Red"
        else:
            color = "Black"
    else:
        color = "Not Sure"
    print (color);