while True:
    entrada_cantidad = input("¿Cuántos números desea ingresar? ")
    if entrada_cantidad.isdigit():
        n = int(entrada_cantidad)
        if n > 0:
            break
        else:
            print("Por favor, ingrese un número mayor a 0.")
    else:
        print("Error: Debe ingresar un número entero válido.")

numeros = []
i = 0
while i < n:
    entrada_num = input(f"Ingrese número {i + 1}: ")
    try:
        num = float(entrada_num)
        numeros.append(num)
        i += 1 
    except ValueError:
        print(f"'{entrada_num}' no es un número válido. Intente de nuevo.")
print(f"\nLista original: {numeros}")
for i in range(n):
    for j in range(0, n - i - 1):
        if numeros[j] > numeros[j + 1]:
            temp = numeros[j]
            numeros[j] = numeros[j + 1]
            numeros[j + 1] = temp
print(f"Lista ordenada: {numeros}")