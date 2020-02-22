
import secrets
import sys


def los_4(n):
    for i in range(1000):
        x = secrets.randbelow(n)
        if x/2 >=500:
            return x
        else:
            continue
def gcd(a, b):
    while a != b:
        if (a > b):
            a = a - b
        else:
            b = b - a
    return a
def isPrime(num):
    prime = True
    if num>1:
        for i in range(2,num//2):
            if num%i==0:
                prime= False
                break
    if prime == True:
        return num
    else:
        return False

def pierwiastki(n):
    pierwiastki = []
    wzglednie_pierwsze  = set(num for num in range(1,n) if gcd(num,n))
    for g in range(1,n):
        zbior = set(pow(g,power)%n for power in range(1,n))
        if wzglednie_pierwsze==zbior:
            pierwiastki.append(g)
    return pierwiastki[-1:]

jawnaPierwsza = isPrime(secrets.randbelow(200))
jawnyRoot = pierwiastki(jawnaPierwsza)
if jawnaPierwsza==False:
    print("Nie wylosowano liczby pierwszej, wylosowano ")
    sys.exit()
for i in jawnyRoot:
    jawnyPierwiastek=0
    jawnyPierwiastek = i





print("Jawne wartosci")
print("Jawna liczba pierwsza, ustalona przez Alicje, Boba i Cezarego: ",jawnaPierwsza)
print("Jawny pierwiastek pierwiotny, ustalona przez Alicje, Boba i Cezarego: ",jawnyPierwiastek)

losowaAlicji = los_4(1600)
losowaBoba = los_4(1600)
losowaCezarego = los_4(1600)

X = (jawnyPierwiastek**losowaAlicji)%jawnaPierwsza
Y = (jawnyPierwiastek**losowaBoba)%jawnaPierwsza
Z = (jawnyPierwiastek**losowaCezarego)%jawnaPierwsza

print("Alicja wysyla X do Boba: " + str(X) + "\n")
print("Bob wysyla Y do Cezarego: " + str(Y) + "\n")
print("Cezary wysyla Z do Alicji: " + str(Z) + "\n")

Zprim = (Z**losowaAlicji)%jawnaPierwsza
Xprim = (X**losowaBoba)%jawnaPierwsza
Yprim = (Y**losowaCezarego)%jawnaPierwsza

print("Alicja wysyla Zprim do Boba: " + str(Zprim) + "\n")
print("Bob wysyla Xprim do Cezarego: " + str(Xprim) + "\n")
print("Cezary wysyla Yprim do Alicji: " + str(Yprim) + "\n")

kAlicji = (Yprim**losowaAlicji)%jawnaPierwsza
kBoba = (Zprim**losowaBoba)%jawnaPierwsza
kCezarego = (Xprim**losowaCezarego)%jawnaPierwsza

print(str(kAlicji) + "\n")
print(str(kBoba) + "\n")
print(str(kCezarego) + "\n")
