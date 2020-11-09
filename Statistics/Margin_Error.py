import math


def margin_error(data):
    try:
        n = len(data)
        p = 0.5
        p1 = 1-0.5
        z = 1.96
        t1 = p * p1
        t2 = round((n/t1), 2)
        t3 = math.sqrt(t2)
        moe = z * t3
        return moe
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
