class TheExample:
    def __init__ (self):
        self.func4 ()


    def func(self):
        return self.a + self.b


    def func1(self):
        return self.a - self.b


    def func2(self):
        return self.a * self.b


    def func3(self):
        if self.b == 0:
            return "error"
        else:
            return self.a / self.b


    def func4 (self):
        self.a = int(input())
        self.b = int(input())

while True:
    print("+, -, *, /")
    x = input()
    print("numbers: ")
    exanple = TheExample()
    if x == "0":
        break
    if x == "+":
        print(exanple.func())
    if x == "-":
        print(exanple.func1())
    if x == "*":
        print(exanple.func2())
    if x == "/":
        print(exanple.func3())


