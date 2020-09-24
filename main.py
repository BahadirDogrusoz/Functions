def ekrana_yazdir():
    print("Ben bir fonksiyonum")

ekrana_yazdir()

print("----------------------------------------------------")

def karesini_al(x):
    print(x * x)

number = int(input("Karesi alınacak sayıyı giriniz: "))
karesini_al(number)

print("----------------------------------------------------")

def toplama(z,t):
    return z + t

print(toplama(10,20))

print("----------------------------------------------------")

us_al = lambda a,b:a**b

print(us_al(2,4))