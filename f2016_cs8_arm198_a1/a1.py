# name       : Arun Mohan
# email      : arm198@pitt.edu
# date       : 9/27/16
# class      : CS0008-f2016
# instructor : Max Novelli (man8@pitt.edu)
#
# Description:
# Assignment 1, program that helps the user understand their gas mileage

# Here I ask the user what system to use
system = input("Enter 'U' to use USC or 'M' to use Metric: ");
# Here I check if the user picked USC and ask for their info in those units
if (system == "U" or system == "u"):
    miles = float(input("Enter the amount of miles traveled using only numbers: "))
    gallons = float(input("Enter how many gallons were used using only numbers: "))
# Here I convert USC to Metric
    km = miles*1.60934
    liters = gallons*3.78541
# Here I checked if the user picked Metric and ask for their info in those units
elif (system == "M" or system == "m"):
    km = float(input("Enter the amount of kilometers traveled using only numbers: "))
    liters = float(input("Enter how many liters were used using only numbers: "))
# Here I convert Metric to USC
    miles = km * 0.621371
    gallons = liters * 0.264172
#Here I tell the user if their input was invalid
else:
    print("Sorry, Invalid Input!");
    exit();
# I calculate fuel consumption in both units
mpg = miles/gallons;
lpk = (100*liters)/km; #lpk equals liters per kilometers; consumption in metric
# I find the user's efficiency
if (lpk > 20):
    rating = "Extremely Poor"
elif (lpk > 15 and lpk <= 20):
    rating = "Poor"
elif (lpk > 10 and lpk <= 15):
    rating = "Average"
elif (lpk > 8 and lpk <= 10):
    rating = "Good"
else:
    rating = "Excellent"
# Here I print all the information in the correct format
print (format("", '32s'), format("USC", '19s'), "Metric");
print (format("Distance", '22s'), ":", format(miles, '11.3f'), "miles",\
       format(km, '16.3f'), "Km");
print (format("Gas", '22s'), ":", format(gallons, '11.3f'), "gallons",\
       format(liters, '14.3f'), "Liters");
print (format("Consumption", '22s'), ":", format(mpg, '11.3f'), "mpg",\
       format(lpk, '18.3f'), "l/100Km");
print ("\nGas Consumption Rating :", rating);