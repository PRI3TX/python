age = int(input("Ingrese su edad en años porfavor: "))
gener = input("Ingrese su genero en minusculas (Ej:masculino / femenino): ")

if (gener == "masculino"):
    pension = 61
    if age == 61:
        print("Te felizito te pensionas este año")
    elif age > 61:
        print("En hora buena ya estas pensionado")
    elif age < 61:
        pension = pension - age
        print(f"Todavia no te has pensionado,pero tranquilo te faltan {pension} años")
elif (gener == "femenino"):
    pension = 57
    if age == 57:
        print("Te felizito te pensionas este año")
    elif age > 57:
        print("En hora buena ya estas pensionado")
    elif age < 57:
        pension = pension - age
        print(f"Todavia no te has pensionado,pero tranquila te faltan {pension} años")
else:
    print("Lo siento no te entiendo, talvez ingresaste mal tu genero recuerda que debe ser todo en minusculas y masculino o femenino")