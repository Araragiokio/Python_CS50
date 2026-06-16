
def main():
    hello()
    name = input("What is your name? ")
    hello(name)

#you can define a function in bottom also

def hello(name="world"):
    """Greet user by name."""
    print(f"Hello, {name}!")    

main()