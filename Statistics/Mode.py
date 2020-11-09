from collections import Counter


def mode(data):
    try:
        c = Counter(data)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
    except ZeroDivisionError:
        print("ERROR: Can't divide by zero")
    except ValueError:
        print("ERROR: Check your input value")
