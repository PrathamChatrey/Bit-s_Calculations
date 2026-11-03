# with built-in function

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

num1 = int(a, 2)
num2 = int(b, 2)

sum = num1 + num2

result = bin(sum)[2:]

print("Addition of binary numbers:", result)

# without built-in function

a = input("Enter first binary number: ")
b = input("Enter second binary number: ")

i = len(a) - 1
j = len(b) - 1

carry = 0
result = ""

while i >= 0 or j >= 0 or carry:

    x = int(a[i]) if i >= 0 else 0
    y = int(b[j]) if j >= 0 else 0

    total = x + y + carry

    result = str(total % 2) + result
    carry = total // 2

    i -= 1
    j -= 1

print("Addition of binary numbers:", result)
