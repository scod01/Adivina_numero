from random import randint

jugador = input("Cual es tu nombre?: ")
numero = randint(1,100)
vidas = 8
intentos = 0

print(f"“Bueno, {jugador}, he pensado un número entre 1 y 100, "
              f"\n y tienes solo ocho intentos para adivinar cuál crees que es el número")
while intentos < 8:
    try:
        intento = int(input("Introduce tu numero: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    if intento < 1 or intento > 100:
        print("Has elegido un numero no permitido")
        continue

    intentos += 1
    vidas -= 1

    if intento < numero:
        print(f"El numero {intento} es incorrecto porque es menor al numero secreto")
    elif intento > numero:
        print(f"El numero {intento} es incorrecto porque es mayor al numero secreto")
    else:
        print(f"Enhorabuena {jugador}, has acertado el numero secreto")
        print(f"Has gastado {intentos} intento(s)")
        break

if vidas == 0:
        print(f"Lo siento {jugador}, te has quedado sin intentos,"
              f"el numero era {numero}")
        print("GAME OVER")

