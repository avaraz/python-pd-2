#zad 14 liczy pierwiastek i wyrzuca błąd przy liczbach ujemnych
import math

try:
    x = int(input("Podaj liczbę: "))
    if x < 0:
        raise ValueError
    else:
        print(f"Pierwiastek z {x} wynosi: ", math.sqrt(x))
except ValueError:
    print("X musi być większy niż 0.")

