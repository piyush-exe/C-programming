print("=============CALCULATOR==== ")

n1 = int(input('Enter first number: '))
oparetor = input("Enter oparetors
(+,-,*,/): ")
n2 = int(input('Enter second number: '))

if oparetor == "+": 
    print(n1 + n2)
elif oparetor == "-":
     print(n1 - n2)
elif oparetor == "*":
     print(n1 * n2)
elif oparetor == "/":
    print(n1 / n2)

else:
    print("Not valid oparetor")