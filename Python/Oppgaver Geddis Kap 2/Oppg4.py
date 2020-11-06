tax_rate=0.07
prices = list(map(int,input("Enter the price of each item, seperated by a space. Hit enter to complete ").split()))
prices_total=sum(prices)
sales_tax=prices_total*tax_rate
sum_total=sales_tax+prices_total

print("Subtotal:",prices_total)
print("Sales tax:",sales_tax)
print("End total:",sum_total)
