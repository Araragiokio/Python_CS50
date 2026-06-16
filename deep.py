ans = input("what is the answer to the Great Question of Life, the Universe, and Everything?").lower().strip()
if ans == "42":
    print("Yes")
elif ans == "forty-two" or ans == "forty two":
    print("Yes")
else:
    print("No")