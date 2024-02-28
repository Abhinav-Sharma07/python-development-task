from cardHolder import cardHolder

def print_menu():
    ### Print options to the user
    print("please choose from one of the the following options...")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4.Exit")

def deposit(cardHolder):
 try:
    deposit= float(input("How much money would you like to deposit: "))
    cardHolder.set_balance(cardHolder.get_balance() + deposit)
    print("Thank for your money. Your new balnce is : ",str(cardHolder.get_balance()))
 except:
    print("Invalid Input")

def withdraw(cardHolder):
   try:
      withdraw= float(input("How much money would you like to withdraw: ",))
      ### Check if user has enough money
      if(cardHolder.get_balance() < withdraw):
            print("Insufficient balance :(")
      else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("You're good to go ! Thank you :)") 
         
   except:
      print("Invalid Input")

def check_balance(cardHolder):
    print("Your current balance is :", cardHolder.get_balance())

if __name__== "__main__":
    current_user =cardHolder("","","","","")

    ### Create a repo of cardholders
    list_of_cardHolders=[]
    list_of_cardHolders.append(cardHolder("786648485676", 8794, "Ashneer", "Grover", 78498746))
    list_of_cardHolders.append(cardHolder("564759823478", 6741, "Mukesh", "Ambani", 1112726))
    list_of_cardHolders.append(cardHolder("356711865187", 7839, "Abhinav", "Sharma", 55000))
    list_of_cardHolders.append(cardHolder("748671347435", 8794, "Virat", "Kohli", 2784671))
    list_of_cardHolders.append(cardHolder("475973146789", 1223, "Elon", "Musk", 999774576))
    
    ### Prompt user for Debit card number
    debitCardNum=""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            ### Check against repo     
            debitMatch=[holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum ]
            if (len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number is not recognized. Please try again.")
        except:
            print("Card number is not recognized. Please try again.")

    ### Prompt for PIN
    while True:
        try:
            userPin=int(input("Please enter your pin : ").strip())
            if(current_user.get_pin() == userPin):
                break
            else:
                print("Invalid Pin. Please try again.1")
        except:
            print("Invalid PIN. Please try again.2")

    ### Print options 
    print("Welcome", current_user.get_firstname(), " :)")
    option = 0
    while (True):
        print_menu() 
        try:
            option = int(input())  
        except:
            print("Invalid input. Please try again.")  

        if(option == 1):
            deposit(current_user)
            break
        elif(option == 2):
            withdraw(current_user)
            break
        elif(option == 3):
           check_balance(current_user)
           break
        elif(option == 4):
            break
        else:
            option=0
        print("Thank you. Have a nice day :) ")
        