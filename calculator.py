#x = input("what's x? ")
#y = input("what's y? ")
#this is wrong
#z = x + y
# because here they are treated as strings and not numbers
#so we need to convert them to numbers first
#z = int(x) + int(y)

#or

x=float(input("what's x? "))
y= float(input("what's y? "))
#if you want to round off the decimal part
z = round(x+y)
print(f"{z:,}")
a = x/y
#a = round(x/y, 2)
#HERE 2 is the number of decimal places we want to round to
print(f"{a:,.2f}")
# the , in the format specifier is used to add commas as thousands separators in the output