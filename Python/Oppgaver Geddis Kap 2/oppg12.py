stock_amt_bought=2000
stock_amt_sold=2000
stock_price_buy=40
stock_price_sell=42.75
commission_rate_buy=0.03
commission_rate_sell=0.03

#price of stock 
buy_total_pre_commmission=stock_amt_bought*stock_price_buy

#commission on first purchase
buy_commission=buy_total_pre_commmission*commission_rate_buy

print("Joe paid his broker $",buy_commission,"for the initial purchase of 2000 shares for a grand sum of: $",buy_total_pre_commmission)

#sale calculation
sales_total_pre_commission=stock_amt_sold*stock_price_sell

#commission on sale
sales_commission=sales_total_pre_commission*commission_rate_sell

print("Joe paid his broker: $",sales_commission,"for his sale of 2000 stocks for a total value of: $", sales_total_pre_commission)

#find profit if no commission were paid
pre_commission_profit=sales_total_pre_commission-buy_total_pre_commmission

print("Before commission, Joe made a profit of: $",pre_commission_profit)

#find total commission for both transactions
commission_total=buy_commission+sales_commission

print("Joe paid his broker a total of:",commission_total)

#find end result after commission
end_result=pre_commission_profit-commission_total

#alternative output based on bottom line
if end_result > 0:
    print("Joe profited a total of: $",end_result,"after paying his broker")
else:
    print("Joe lost a grand total of: $",end_result,"on his stock adventrure")