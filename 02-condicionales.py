#Entrada
print ("MI CALCULADORA")
numero1 = input ("Numero 1: ")
numero2 = input ("Numero 2: ")
operacion = input ("Ingrese el tipo de operacion (suma|resta): ")

#Proceso
if operacion == "suma":
    resultado = int(numero1) + int(numero2)
    #Salida
    print ("La suma es: " + numero1 + " + " + numero2 + " = " + str(resultado))
elif operacion == "resta":
    resultado = int(numero1) - int(numero2)
    #Salida
    print ("La resta es: " + numero1 + " - " + numero2 + " = " + str(resultado))
else:
    print ("Operacion no existe")
    