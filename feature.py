print("feature")


def greet(message, name):
    print(r"hello, {name}. {message}.")


def bow():
    print("Bow!")


def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def divide(a, b):
    return a / b


def mod():
    pass


if __name__ == "__main__":
    fizzbuzz(20)
    print(add(3, 5))
    print(sub(10, 4))
    print(mul(2, 3))
    print(divide(10, 2))
    print("let's feature branch!")
