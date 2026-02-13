#If cost price and selling price of an item is input through the keyboard,
# write a program to determine whether the seller has keyboard,
# write a program to determine whether the seller has
#made profit or incurred loss.
# Also determine how much profit he made or loss he incurred.

cp = float(input("Enter your Cost Price: "))
sp = float(input("Enter your Selling Price: "))
pro_loss = sp - cp
if pro_loss < 0:
    print(f"You incurred a Loss of ${pro_loss}")
elif pro_loss > 0:
    print(f"You made a Profit of ${pro_loss}")
else:
    print(f"You made NO PROFIT ", pro_loss)
    