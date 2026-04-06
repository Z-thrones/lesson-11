units = int(input("Please enter how much units of electricity you used this month:  "))
if units < 50:
    amount = units * 2.60
    surcharge = 25
    ta1 = amount + surcharge
    print("Your electricity bill is " , ta1)
elif units > 50 and units < 100:
    amount2 = 130 + units * 3.25
    surcharge2 = 35
    ta2 = amount2 + surcharge2
    print("Your electricity bill is " , ta2)
elif units > 100 and units < 200:
    amount3 = 130 + units * 5.26
    surcharge3 = 45
    ta3 = amount3 + surcharge3
    print("Your electricity bill is " , ta3)
else:
    amount4 = 130 + units * 8.45
    surcharge = 75
    ta4 = amount4 + surcharge
    print("Your electricity bill is" , ta4)