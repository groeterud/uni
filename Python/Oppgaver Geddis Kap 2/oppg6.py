prcnt=1.05
amt=int(input("Please specify total amount of purchase: "))
instalments=int(input("Please enter a number of instalements: "))
total=amt*prcnt
instalments_total=total/instalments

print("Your grand total is:",total)
print("To be paid in", instalments,"instalments of:",instalments_total)