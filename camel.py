def snake_case(camel_case):
   snake_case = ""
   for char in camel_case:
      if char.isupper():
         snake_case += "_" + char.lower()
      else:
         snake_case += char
   print(f"snake_case: {snake_case}")


def main():
   camel_case = input("Enter a camelCase string: ").strip()
   snake_case(camel_case)

main()