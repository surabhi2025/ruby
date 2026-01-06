Total_Bill = 2.50
Paid = 4
due_amount = Paid - Total_Bill


while due_amount:
    if due_amount>0:
        print("You have to give", due_amount)
        due_amount = 0
        break
    elif due_amount<0:
        print("Perfect, they paid the right amount")
        
    else:
        print("bye")