# In This Example I will make a GCD Calculator.
# This calculator calculate GCD of numbers you give.
# No Limit For Numbers
# Enjoy !
# 6 12 15
def GCD_Calculator(*args):
    ourGCD = 1
    ourMinNumber = min(args)
    ourDividerListNotEdited = list(range(ourMinNumber+1))
    ourDividerList = ourDividerListNotEdited.remove(0)
    
    numbers = args

    currentStatus = False

    for divider in ourDividerList:
        for number in numbers:
            if number % divider != 0:
                break
            else:
                ourGCD = divider
    return ourGCD


print(GCD_Calculator(6,12,15))


    

   



            
            
            


    
   
   

    





    



    
        
        




