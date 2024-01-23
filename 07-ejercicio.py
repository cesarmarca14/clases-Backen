# Entrada
bandera = "si"
num = int(input("Ingrese un número: "))

# Proceso y Salida
for i in range(num):
    if i == 0 or i == num - 1:
        print('*' * num)  # Imprime la primera y última línea
    else:
        print('*' + ' ' * (num - 2) + '*')  # Imprime las líneas intermedias

        bamdera = input("Desea continuar? (si|no): ")
        