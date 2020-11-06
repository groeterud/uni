males_input=int(input("How many boys are in the class?"))
females_input=int(input("How many girls are in the class?"))
total=males_input+females_input
#calculations
males_pct=males_input/total*100
females_pct=females_input/total*100

males_round=round(males_pct,2)
females_round=round(females_pct,2)

print("males percentage:",males_round)
print("females percentage:",females_round)