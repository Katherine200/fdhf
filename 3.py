#Problema: Definir una funcion que genere_n_caracteres() que tome como entreda un enrero n y un carácter
#Entradas: Numero de caracteres (entero) y caracter (cadena)
#Salidas: Cantidad de caracteres segun el numero dado para su repeticion (n_caracteres*caracter (cadena))
#Restricciones:Numero de caracteres mayor a cero

#Procedimiento:
#1) Determinar el numero de caracteres
#2) Determinar el caracter
#3) Multiplicar el numero de caracteres por el caracter dado
#4) Retornar el resultado


def caracter(Numerodecaracteres,Caracter):
    A=int(Numerodecaracteres)
    B=str(Caracter)

    C= A*B
    return C
    

    
