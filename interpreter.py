exp = input("Enter an expression: ").strip()
first, second, third = exp.split(" ")
if second == "+":
    result = float(first) + float(third)
    print(f"{result:.1f}")
elif second == "-":
    result = float(first) - float(third)
    print(f"{result:.1f}")
elif second == "*":
    result = float(first) * float(third)
    print(f"{result:.1f}")
elif second == "/":
    if third == "0":
        print("Error: Division by zero")
        
    result = float(first) / float(third)
    print(f"{result:.1f}")