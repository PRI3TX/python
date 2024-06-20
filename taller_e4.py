print("*"*50)
print("Ejercicio 4")
print("Bienvenido aqui podras saber determinar si un numero es negativo o positivo")
n_user = float(input("ingrese su numero "))
if n_user < 0:
    print("Negativo")
elif n_user == 0:
    print("El numero es 0")
else:
    print("Positivo")