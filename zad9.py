#zad 9 wczytuje liczbę wielocyfrową i sumuje jej cyfry
x = int(input("Podaj liczbę wielocyfrową: "))
 
suma = 0
 
while x != 0:
  suma += x%10
  x //= 10
print(suma)