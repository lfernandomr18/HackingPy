archivo=open("archivo1.txt","a")

dedicacion= input("dedicacion: ")
empresa= input("empresa: ")
idioma= input("idioma: ")

archivo.write(dedicacion)
archivo.write("\n")
archivo.write(empresa)
archivo.write("\n")
archivo.write(idioma)
archivo.write("\n")

archivo.close()