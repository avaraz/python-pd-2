#zad 8 wczytuje liczby i umieszcza je na liście przy użyciu pętli while
ile = int(input("Podaj dlugość listy: "))
lista = []
 
i = 0
while i < ile:
  i += 1
  x = int(input("Podaj liczbę: "))
  lista.append(str(x))
print(lista)