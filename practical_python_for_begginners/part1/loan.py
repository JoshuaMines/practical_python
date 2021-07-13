
#get the loan details
money_owed = float(input("how much money do you owe?\n")) #$50,000
apr = float(input("what is your rate?")) #3%
payments = float(input("what will your monthly payment be, in dollar?\n")) #$1,000
months = int(input("how many months do you want to see results")) #24

# divide apr by 100 to make it a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
    #add in interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payments < 0):
        print('the last payment is', money_owed)
        print('you paid off the loan in', i+1, "month")
        break #break takes you out of the loop and runs everything out of it

    #make payment
    money_owed = money_owed - payments

    #print the results after this
    print("paid", payments, "of which", interest_paid, "was interest", end=' ')
    print("now i owe", money_owed)