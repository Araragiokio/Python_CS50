amount = 50
total = 0
print(f"Amount due: {amount}")
while total<50 :
    coin = int(input("Insert coin: "))
    if coin in [25, 10, 5]:
        total = total + coin
        if amount > coin:
            amount = amount - coin
            print(f"Amount due: {amount}")
        elif amount == coin:
            amount = amount - coin
            print("Change owed: 0")
        else:
            change = coin - amount
            print(f"Change owed: {change}")
    else:
        print(f"Amount due: {amount}")
    