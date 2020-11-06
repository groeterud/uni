purchase_amt=int(input("Enter desired package ammount to calculate possibly discounts: "))

software_price=99

if purchase_amt>0:
    if purchase_amt>10:
        discount=0
    else:
        if purchase_amt>20:
            discount=0.1
        else:
            if purchase_amt>50:
                discount=0.2
            else:
                if purchase_amt>100:
                    discount=0.3
                else:
                    discount=0.4
#end loop 

discount_amt=(purchase_amt*software_price)*discount
print("Your discount is:",format(discount_amt,".2f"))

sum_total=(purchase_amt*software_price)-discount_amt
print("Total price for your purchase is:",sum_total)
