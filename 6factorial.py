def fact(n):
    if n == 0 or n == 1:
        return 1
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

num = int(input("Enter a number: "))
result = fact(num)
print(f"The factorial of {num} is: {result}")
