#zad 15 błąd zmiennych

try:
   x = int(input("Podaj liczbę: "))
   print(x)
except ValueError:
    print("X musi być integerem.")

    