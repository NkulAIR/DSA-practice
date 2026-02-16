def main():
    print(factorial(5))
    print(fibonacci(5))

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
    

main()