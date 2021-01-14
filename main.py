def calculate(option,x,y):
    if "add":
        return x + y
    elif "subtract":
        return x - y
    elif "multiply":
        return x * y
    else:
        return x / y

print (calculate("subtract",10,5))