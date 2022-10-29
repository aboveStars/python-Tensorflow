print(
"""
    In This Example I made a GCD Calculator.
This calculator calculate GCD of numbers you give.
    No Limit For Numbers If You Want To Stop Just Enter
Enjoy!

"""
)


def GCD_Calculator(args):
    dividers = list(range(min(args)+1))
    dividers.remove(0)
    dividers.sort(reverse=True)

    for divider in dividers:
        resultList = [n%divider for n in args]

        if resultList.count(0) == len(resultList):
            return f"\nGCD is : {divider}"
        else:
            print(f"\nTried Number: {divider}")
            print(f"Also our bad-result-list = {resultList}")


givenArgs = []
indexOfInput = 1

while True:
    x = input(f"Give {indexOfInput}. Number: ")
    if x:
        givenArgs.append(int(x))
        indexOfInput += 1
    else:
        break

print(GCD_Calculator(givenArgs))
