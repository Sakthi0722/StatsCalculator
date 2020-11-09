def mean(data):
    try:
        a = sum(data)
        b = len(data)
        c = a / b
        return c
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
