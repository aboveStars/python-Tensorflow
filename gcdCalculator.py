print(
    """
    In This Example I will make a GCD Calculator.
    This calculator calculate GCD of numbers you give.
    No Limit For Numbers
    Enjoy !
    """
)


def GCD_Calculator(*args):
    dividers = list(range(min(args)+1))
    dividers.remove(0)
    dividers.sort(reverse=True)

    for divider in dividers:
        resultList = [n%divider for n in args]

        if resultList.count(0) == len(resultList):
            return f"GCD is : {divider}"
        else:
            print(f"Tried Number: {divider}")
            print(f"Also our bad-result-list = {resultList}")



print(GCD_Calculator(5,10,15))
