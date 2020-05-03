#zad 2 pobiera liczby i mnoży je przez siebie, wyświetlanie przy użyciu sys
import sys
print("Podaj 2 liczby: ")
x = sys.stdin.readline()
y = sys.stdin.readline()
x = int(x)
y = int(y)
z = x*y
print("Twoj wynik to: ")
sys.stdout.write(str(z))
