# instagram-->if account is private--> if both are frnds-->u can send message.
#if account is public--->send message directly.
# if  account is private---> both not frnds--> u cant send msg.





is_account_private=True
are_friends=False
allow_everyone=False


if is_account_private:
    if are_friends:
        print("can send message directly")
    else:
        print("can not send a message")
else:
     if allow_everyone:
        print("anyone can send message without following")
     else:
         print("only frns can send message until he/she accept your message request")



#first we will check whether they r frnds are not.
#if they r frnds---> directly send message.
#if they r not frnds-->need to check account is private and public.
#if account is private --->cant send message directly without following
#if account is public--->need to check allowing everyone or not.
#if allows everyone then send message.
#if not only frnds can send message until they accept ur message request.




if are_friends:
    print("send messagedirectly")
else:
    if is_account_private:
        print("they can not send the message")
    else:
        if allow_everyone :
            print("everyone can send the message")
        else:
            print("only frnds can send message until they accept ur message")



     #if purchase amount is greater than or equal to 500 then delivary will be free.
     # if not then  delivary fee will be charges 50rs by defult
     # purchase amount should be calculated based on the item price and quantity
     # if distance is more than 3kms then need to add 10rs extra.                 




price=int(input("enter item price :"))
quantity=int(input("enter the quality :"))
purchase=quantity*price
distance=int(input("enter the distance :)"))

if distance<=3 and purchase >=500:
    print("no extra charge for delivary")
else:
    if purchase <500: 
        if distance<=3: 
            print("extra 50rs will be added in the bill")
        elif distance>=3:
            extra_distance=distance-3
            total_delivary=distancefee=extra_distance*10+50
            print(f"amount of {total_delivary} will be added to the bill")
        else:
            print("no delivary fee")  


        if purchase >=500:
            print("no extra charge for delivary")
        else:
                if distance<=3:
                    print("extra 50rs will be added in the bill")
                else:
                    print(f" amount of{(distance-3)*10+50} will be added to the bill")   

                        



#limit_avaliable
#spending_amount--> checks the limit and can spend the amount. 
#once u spend the amount--> then limit should be reduced and due amount should be incerese.
#pay the bill--> limit should be incerese and then due  should be reduced.


   
    




                    
                    

