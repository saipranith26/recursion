#  recurssive implementation of Factorial
def Factorial(num):
    if num == 1:
        return 1
    else :
        temp = num * Factorial(num-1)
    return temp
print(Factorial(100))
