sugar=1.5
butter=1
flour=2.75

#mats are for 48 cookies. Need to bring them down to values per 1
raw_modifier=48

sugar_raw=sugar/raw_modifier
butter_raw=butter/raw_modifier
flour_raw=flour/raw_modifier


#get input from user
amt_cookies=int(input("How many cookies do you want to make?"))

#calculation
sugar_actual=sugar_raw*amt_cookies
butter_actual=butter_raw*amt_cookies
flour_actual=flour_raw*amt_cookies

#rounding to limit decimal places
sugar_round=round(sugar_actual,2)
butter_round=round(butter_actual,2)
flour_round=round(flour_actual,2)

#return value to user
print("You are going to need:",sugar_round,"cups of sugar.")
print(butter_round,"cups of butter")
print(flour_round,"cups of flour")


