num1 = float(input("first number: "))
num2 = float(input("second number: "))
result = num1 * num2
print(f"{int(num1)} x {int(num2)} = {int(result)}")
if result > 0:
    print("The result is positive")
elif result < 0:
    print("The result is negative")
else:
    print("The result is zero")