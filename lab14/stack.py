class MyException(Exception):
    pass


def divide(a, b=0):
    return a / b


def decide(do=True):
    if do:
        return divide(1)
    else:
        return divide(1, 1)


def start():
    decide()


start()

## alalyze stacktrace
## break if b == 1
## break if ZeroDivisionError


try:
    start()
except ZeroDivisionError as e:
    print("Something went wrong", e)
finally:
    print("Always work")
