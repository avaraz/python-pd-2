#zad 5 pobiera liczby i sprawdza warunki
a,b,c = input("Podaj 3 liczby:"),input(),input()

a = int(a)
b = int(b)
c = int(c)

if a>0 and a<=10:
    if a>b and b>c:
        print("A spełnia podane warunki.")
    else:
        print("A nie spełnia podanych warunków.")
else:
    print("A nie spełnia podanych warunków.")