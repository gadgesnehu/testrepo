sum = 0
while (True):
    userInput = input("Enter the price:\n")
    if (userInput!= 'q'):
        sum = sum + int(userInput)

    else: 
        print("")
        print(f"Your total bill is {sum}.Thanks for using our calculator")
        break     

      