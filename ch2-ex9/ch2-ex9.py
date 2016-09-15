

temp = (int(input("Enter a temperature in Fahrenheit \
or Celsius using only integers: ")));
temp = (input("Enter 'F' or 'f' if the temperature is in Fahrenheit \
\nor 'C' or 'c' if the temperature is in Celsius: \n"));
if temp == "F" or temp == "f":
    convert1 = 5*(cels - 32)/9
    unit = "Fahrenheit"
    unit2 = "Celsius"
else:
    convert1 = (9/5)*cels + 32;
    unit = "Celsius"
    unit2 = "Fahrenheit"
print ("You entered", cels, "degrees", unit,\
    "\nThat is equal to", convert1, "degrees", unit2);