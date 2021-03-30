#Example 1

import math# I am importing the inbuilt math
total_amount=0# I am also starting the total amount on zero

print ("Choose either 'investment' or 'bond' from the menu below to procceed")# I want the user to konw which options he has
print ("investmnet   - to calculate the amount of interest you'll earn on interest")#I am giving the user an explanation on what his options are and giving him/her the definition
print ("bond         - to calculate the amount you'll have to pay on a home loan")#I am giving the user an explanation on what his options are and giving him/her the definition
choice = input("What is your choice 'investmnet' or 'bond'? : ")#The user can choose the choice between investmen and bond

if choice.lower() == 'investment':# If the user chooses investment
    deposit = float (input ("What is the amount of money that you want to deposit?: "))#Than the question of amount he wants to invest should come up
    interest_rate = float (input ("Please enter the interest rate as the percentage : "))#The user should enter the interest that is given
    number_of_years = int (input ("How many years are you planning to invest?: "))#The user should tell us the amount of years he is will to invest
    interest = input ("Do you want 'simple interest' or 'compund interest'?: ") #The user has 2 options to choose from simple or compund interest
    interest_rate = interest_rate / 100# we also need to divide the interest rate by 100 so that we know  the percentage

    if interest.lower() == 'simple interest':# if the user chooses simple interest
        total_amount = deposit*(1 + interest_rate * number_of_years)# if the user chooses simple interest
        print (total_amount)# And the amound that he will make will be given
        
    if interest.lower() == "compound interest":## if the user chooses compund interest
        total_amount = deposit* math.pow((1+interest_rate),number_of_years)# Than this formulae should be given
        round (total_amount) #Since there will be more decimals we want to round of the figure
        print (total_amount)# And the amound that he will make will be given
        
if choice.lower () == 'bond':#If the user chooses bond
      p = float (input ("What is the current value of your house?: "))#Than we should ask for the current value of the house
      i = float (input ("Please enter the interest rate of percent: "))#The user should also give us the interest rate of the bond
      n = int (input ("How many years are you planning to pay?: "))#The use should tell us how many years are the going to pay
      i = i / 100 #We also want to divide the interest by 100 to get the percentage
      repayment = (i*p)/(1-math.pow((1+i),-n))#Than this formulae should be used
      repayment = round (repayment) # We want to round of the figure becauss of the decimal
      print (repayment)#Print the result