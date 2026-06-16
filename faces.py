def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    str = input("Enter a string: ")
    print(convert(str)) 

main()   