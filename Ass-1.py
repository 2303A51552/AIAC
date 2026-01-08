#Generate a python code to check whether a given number is prime or not without using functions and the program must be able to take the dynamic input
num = int(input("Enter a number: "))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
#Optimize the above code for better functionality with using function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

#Give iterative code for fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

num = int(input("Enter the number of terms for Fibonacci series: "))
fibonacci(num)

#Generate recursion code as the optimized version of the above code
def fibonacci_recursive(n, a=0, b=1):
    if n > 0:
        print(a, end=" ")
        fibonacci_recursive(n - 1, b, a + b)
    else:
        print()
num = int(input("Enter the number of terms for Fibonacci series: "))
fibonacci_recursive(num)    
