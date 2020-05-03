#zad 10 rysowanie wieży z liter "A"
n = int(input("Jak wysoka ma być wieża? "))
 
if n <= 10 and n > 0:
  for i in range(n):
    print("A"*(i+1))
else:
    print("Wieża jest zbyt wysoka lub niska.")
