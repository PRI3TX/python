
import random

vidas = 4

jugada_1 = "piedra"
jugada_2 = "papel"
jugada_3 = "tijera"
print("Bienvenido usuario")
print(f"Cuentas con {vidas} vidas cada que pierdas una partida "
  "perderas una vida y cada que  ganes ganaras una vida")


while vidas > 0:
    
    jugada_persona = input("Piedra, papel o tijera? ").lower()
    jugada_pc = random.choice([jugada_1, jugada_2, jugada_3])
    print("La jugada del pc es: " + jugada_pc)
    if jugada_pc == jugada_persona:
        print("Empate")
        print(f" tienes {vidas} vidas")
    elif jugada_persona > jugada_pc:
        print("Ganaste")
        vidas += 1
        print(f" tienes {vidas} vidas")
    elif jugada_persona < jugada_pc:
        print("Perdiste")
        vidas -= 1
        print(f" tienes {vidas} vidas")
    elif not(jugada_persona  in jugada_pc):
        print("Valor no válido -1 vida")
        vidas -= 1
        print(f" tienes {vidas} vidas")
  
# Mensaje de fin de juego
print("-" * 50)
print(f" tienes {vidas} vidas")
print("GAME OVER")
print("-" * 50)