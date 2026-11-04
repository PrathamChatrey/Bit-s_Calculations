# with built-in function

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

num1 = int(a, 2)
num2 = int(b, 2)

result = num1 - num2

print("Subtraction in binary:", bin(result)[2:])

# without built-in function

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

num1 = 0
num2 = 0

for i in a:
    num1 = num1 * 2 + int(i)

for i in b:
    num2 = num2 * 2 + int(i)

result = num1 - num2

binary = ""

if result == 0:
    binary = "0"

while result > 0:
    rem = result % 2
    binary = str(rem) + binary
    result = result // 2

print("Subtraction in binary:", binary)
