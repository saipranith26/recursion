#  recurssive implementation of Fibonacciseries
def Fibonacci(n):
    res =[]
    if n <=1:
        return n
    else :
        return Fibonacci(n-1)+Fibonacci(n-2)

        
print(Fibonacci(10))