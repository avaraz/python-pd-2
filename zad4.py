#zad 4 pobiera liczbę i zamienia ją na liczbę bezwzględną
x = input("Podaj liczbę: ")
x = int(x)

if x < 0:
    x = -x
    print ("Liczba bezwzgledna to:", x)
else:
    print ("Liczba bezwzgledna to:", x)