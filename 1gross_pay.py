def gross_pay_calculation(hrs, rate):
    return hrs * rate

# Get input from the user and convert to float
num1 = float(input("Enter Hours: "))
num2 = float(input("Enter Rate: "))

# Call the function with the input values
Salary = gross_pay_calculation(num1, num2)
print("Your Gross pay is: ", Salary)
