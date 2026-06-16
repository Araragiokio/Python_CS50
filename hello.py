#take user input
name = input("What is your name? ")
#print ("Hello, world!")
print(f"Hello, {name}!")
# f-string is a way to format strings in Python
#
#OR
#
print ("hello, ", end="")
print (name)
# documentation of print = print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#sep is the separator between the objects, end is what to print at the end of the line
#
#OR
#
print ("hello, "+ name) 
#
#OR
# how to print comma and quotes
print ('hello, "friend" '+ name) 