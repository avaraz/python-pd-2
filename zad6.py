#zad 6 wyświetla liczby podzielne przez 5 w podanym zakresie
for x in range(1,25):
    if (x % 5 == 0):
        print(str(x) + " ")
else: 
    print("Koniec listy.")