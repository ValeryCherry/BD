print("Two numbers: ")
a = int(input())
b = int(input())
print("+", "-", "*", "/", "0-exit")
print("operator: ")

def plus (a,b):
    return a + b

def minus (a, b):
    return a-b

def proizv (a, b):
    return a * b

def delen (a,b):
    if b == 0:
        return "error"
    else:
        return a/b
while True:
    x = input()
    if x == 0:
        break
    else:
        if x == "+":
            print("result:", plus(a, b))
        if x == "-":
            print("result:", minus(a, b))
        if x == "*":
            print("result:", proizv(a, b))
        if x == "/":
            print("result:", delen(a, b))
        print("operator: ")




