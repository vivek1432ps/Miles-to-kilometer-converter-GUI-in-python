def add(*args):
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(5, 3, 4, 5, 6, 4, 5))


def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


# calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.modal = kw.get("model")


my_car = Car(make="bmw", )


def py():
    n = 9
    for i in range(n):
        x = i + 1
        y = x * 1
        print((f"{y}" * (i * 2 + 1)).center(n * 10 - 1))


py()
