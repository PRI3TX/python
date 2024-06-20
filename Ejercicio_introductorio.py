a=float(input("ingresela nota del estudiante "))

if a >=0 and a <= 5:
    print("El numero ingresado si esta dentro del rango permitido")
    if a < 3:
        print("se echo la materia =(")
    elif a >= 3 and a <4:
        print("paso pero estudie más")
    else:
        print("paso sobrado pai")
else:
    print("el numero ingresado no esta dentro del rango, no sea bruto")
