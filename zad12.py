#zad 12 tabliczka mnożenia

for x in range(1,11):
    for y in range(1,11):
        print("|",f"{x * y:^4}", end="|\t")
    print()