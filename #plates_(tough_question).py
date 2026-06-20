def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #condition 1: Length check
    if len(s) < 2 or len(s) > 6:
        return False
    #condition 2: First two characters must be letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    #condition 3: Only alphanumeric characters allowed, no punctuation, spaces, or special characters
    if not s.isalnum():
        return False
    #condition 4: Numbers cannot be in the middle
    first_number = False 
    for char in s:
        if char.isalpha():
            if first_number == False:
                continue
            else:   
                 return False
        ##condition 5: If there are numbers, they must be at the end. The first number cannot be '0'    
        if char.isdigit():
            if not first_number:
                if char == '0':
                    return False
    
            first_number = True
    return True     
main()