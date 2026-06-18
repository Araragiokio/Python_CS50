def main():
    input_string = input("Input : ")
    output = twttr(input_string)
    print(f"Output: {output}")

def twttr(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char not in vowels:
            result = result + char
    return result  
 
main()