while True:
    try:
        x, y = input("fraction: ").strip().split("/")
        x, y = int(x), int(y)
        if y == 0:
            raise ZeroDivisionError
        
        elif x < 0 or y < 0:
            raise ValueError("Numerator and denominator must be non-negative.")
        
        elif x > y:
            raise ValueError("Numerator cannot be greater than denominator.")

    except ZeroDivisionError:
        print("Error: Denominator cannot be zero.")

    except ValueError as e:
        print(f"Error: {e}")
        
    else:
        break


percentage = (x / y) * 100
if percentage <= 1:
    print("E")
elif percentage >= 99:
        print("F")
else:
    print(f"Percentage: {percentage:.0f}%")
