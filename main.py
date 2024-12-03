print("Hello World")

#Variables
name = "Dilan"
edad = 23
heigth = 1.68
estudiante = True

#Conjunto de datos
hobbies = ["Manejar moto", "Pintar", "Jugar", "Dibujar"]

#Concatenacion
print(name, "tiene", edad,  "años, mide", heigth, ". Le gusta", hobbies)
print(name, "tiene", edad,  "años, mide", heigth, ". Le gusta", hobbies[2], "pero no le gusta ", hobbies[3])

#Concatenacion con listas
hobbies[1] = input("Ingrese un valor: ")
print(name, "tiene", edad,  "años, mide", heigth, ". Le gusta", hobbies[1])

#Concatenacion con listas hacia atras
dato = input("Ingrese un valor: ")
hobbies.append(dato)
print(name, "tiene", edad,  "años, mide", heigth, ". Le gusta", hobbies[-2])

#Concatenacion y eliminacion de un dato de la lista
hobbies.pop(1)
dato= input("Ingrese un dato: ")
hobbies.append(dato)
print(name, "tiene", edad,  "años, mide", heigth, ". Le gusta", hobbies)