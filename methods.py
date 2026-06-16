name = input("What is your name? ").strip().title()
#here strip and tittle are used to remove any leading/trailing whitespace and capitalize the first letter of each word in the name
#these are string methods that can be used to manipulate the input before printing it out
#method is just an other name used for member functions of a class in python

#spliting the input into sub strings 
first, last = name.split(" ")
#spilt method returns a sequence of strings and we can assign them st the same time from right to left 

print(f"Hello, {first}!")