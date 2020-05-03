# zad 7 pobiera liczby i wyswietla ich kwadraty
ile = int(input("Podaj ile liczb chcesz podniesc do kwadratu: "))
lista = []
 
for i in range(0, ile):
  x = int(input("Podaj liczbe: "))
  x *= x
  lista.append(str(x))
print(lista)