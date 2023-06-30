


archivo=open("wordlist.lst","r")
# forma1
print("forma 1")
for l in archivo.read().split("\n"):
    print(l)
print("*******************************************")
#forma2
archivo2=open("wordlist.lst","r")
print("forma 2")
lista=archivo2.read().split("\n")
for n in lista:
    print(n)
archivo2.close()


