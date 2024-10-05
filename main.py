def cal(bill_amount,tip_per):
    total= bill_amount*(1+0.1*tip_per)
    total= round(total,2)
    print(f"pls pay${total}")
cal(150,2)