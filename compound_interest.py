#Python Program for compound interest
def compound_interest():
    
    amount = principle *(pow(1+rate/100,time))
    CI = amount - principle
    print ("Compound interest is",CI)

principle = float(input("Enter principle value:"))
rate = float(input("Enter the rate:"))
time = float(input("Enter time:"))

compound_interest()



