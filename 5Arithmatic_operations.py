def calc_ops(n1, n2):
    sum_res = n1 + n2
    diff_res = n1 - n2
    prod_res = n1 * n2
    quot_res = n1 / n2 if n2 != 0 else 'undefined'
    
    return sum_res, diff_res, prod_res, quot_res

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_res, diff_res, prod_res, quot_res = calc_ops(num1, num2)

print(f"The sum is: {sum_res}")
print(f"The difference is: {diff_res}")
print(f"The product is: {prod_res}")
print(f"The quotient is: {quot_res}")
