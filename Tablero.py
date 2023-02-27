blanco="[  ]"
negro="[##]"

columnas=int(input("ingrese cantidad de columnas: "))
f=int(input("ingrese cantidad de filas: "))

while f>0:
        linea=""
        if f%2==0: #si f es par
                i=columnas
                while i>0:
                        if i%2==0: #si i es par
                                linea=linea+blanco
                        else:      #si i es impar
                                linea=linea+negro
                        i=i-1
                print(linea)
        else:      #si f es impar
                i=columnas
                while i>0:
                        if i%2==0: #si i es par
                                linea=linea+negro
                        else:      #si i es impar
                                linea=linea+blanco
                        i=i-1
                print(linea)
        f=f-1