amount = int(input("Enter an amount of bolts greater than zero using only integers: "));
inState = input("Enter 'I' if the order is in-state or 'O' if the order is out-of-state: ");
totalCost = amount*0.5;
if (amount <= 1000):
    discount = 0.1
elif (amount > 1000 and amount <= 5000):
    discount = 0.15
elif (amount > 5000 and amount <= 10000):
    discount = 0.2
elif (amount > 10000):
    discount = 0.2 + 0.00001*amount
finalCost = totalCost - amount*discount;
if (inState == "I" or inState == "i"):
    taxRate = 0.1
elif (inState == "O" or inState == "o"):
    taxRate = 0.07
else:
    print ("Asshole");
taxAmount = taxRate*finalCost;
totalAmount = finalCost + taxAmount;
if (amount <= 500):
    ship = 0
elif (amount > 500 and amount <= 1000):
    ship = 0.025
elif (amount > 1000 and amount <= 2000):
    ship = 0.05
elif (amount > 2000 and amount <= 3000):
    ship = 0.075
elif (amount > 3000 and amount <= 4000):
    ship = 0.1
elif (amount > 4000 and amount <= 5000):
    ship = 0.15
elif (amount > 5000 and amount <= 10000):
    ship = 0.2
elif (amount > 10000):
    ship = 800 + ((amount - 10000)//10000)*250
print ("Your cost before discounts is", format(totalCost, ",.3f"), "dollars");
print ("You receive a discount of", format(discount*100, ",.3f"), "percent off.");
print ("Your total cost including the discount is", format(finalCost, ",.3f"), "dollars");
print ("Your tax rate is", format(taxRate*100, ",.3f"), "percent");
print ("Your tax amount is", format(taxAmount, ",.3f"), "dollars");
if (amount > 10000):
    shipRate = .1 * amount - ship
    print ("Your shipping rate is one cent per piece.\n Your shipping discount is", format(ship, ",.3f"), "dollars off")
    print ("Your shipping fee is", format(shipRate, ",.3f"), "dollars")
else:
    shipRate = (.1 * amount) - (ship * amount)
    print ("Your shipping rate is one cent per piece.\n Your shipping discount is", format(ship*100, ",.3f"), "percent off")
    print ("Your shipping fee is", format(shipRate, ",.3f"), "dollars")
print ("Your final cost, with tax and shipping, is", format(totalAmount+shipRate, ",.3f"), "dollars");