numero=int(input("ingrese un numero positivo que quiera sacar el factorial "))
contador = 1
factorial = 1
while contador <= numero:
    factorial = factorial * contador
    contador +=1
    
print("El factorial del numero es ", factorial)