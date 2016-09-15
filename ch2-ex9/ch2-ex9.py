

cels = (int(input("Enter a temperature in Fahrenheit \
or Celsius using only integers: ")));
temp = (input("Enter 'F' or 'f' if the temperature is in Fahrenheit \
\nor 'C' or 'c' if the temperature is in Celsius: \n"));
if temp == "F":
    convert1 = 5*(cels - 32)/9;
elif temp == "f":
    convert1 = 5*(cels - 32)/9;
elif temp == "C":
    convert1 = (9/5)*cels + 32;
elif temp == "c":
    convert1 = (9/5)*cels + 32;
print ("You entered", cels, "degrees Fahrenheit.\n\
    That is equal to", convert1, "degrees Celsius");