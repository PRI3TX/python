print("*"*50)
print("Ejercicio 6")
numero=int(input("ingrese un numero positivo que quiera sacar el factorial "))
contador = 1
factorial = 1
for  i in range(1,1+numero):
    factorial = factorial * contador
    contador +=1
    
print("El factorial del numero es ", factorial)