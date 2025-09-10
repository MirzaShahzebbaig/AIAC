def div(a, b):
    return a / b

try:
    print(div(10, 0))
    print("done")
except ZeroDivisionError:
    print("Error: Division by zero")
    print("done")
except Exception as e:
    print("Error:", e)
    print("done")
