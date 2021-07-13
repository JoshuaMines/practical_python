#def defines function
def addition(a, b):
    return a + b

def main():
    num1 = float(input('enter 1st number:\n'))
    num2 = float(input("enter 2nd numer:\n"))

    result = int(addition(num1, num2))
    print("the sresu is", result)

main()