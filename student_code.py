# LAB Python Intro
# Javier Barroso

#Iteration 1 / Hello_User

nombre = input("Buenas?!, Con quien hablo??: ")

print(f"Que tal estas? {nombre}")

# Iteración 2 / Add_Números

print("Pasame dos numero para SUMAR")
numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
suma = numero1 + numero2
print(f"La suma es : {suma}")

# Iteración 3 / What_is_your_age

import datetime
cumpleaños = input("En que año naciste?: ")
edad = datetime.datetime.today().year - int(cumpleaños)
print(f"Tienes: {edad}")

# Iteración 4 / Even_or_Odd

numero = int(input("Introduce numero: "))
if numero%2 == 0:
    print(f"{numero} es PAR")
else:
    print(f"{numero} es IMPAR")

# Iteración 5 / Conde_to_Ten

for i in range(10):
    print(i+1)
    
# Iteración 6 / Multiplicación_Table

multiplicar = int(input("Tabla de Multiplicar del: "))

for i in range(10):
    print(f"{multiplicar} X {i+1} = {multiplicar * (i+1)}")

# Iteración 7 / What_can_i_drink

edad = int(input("Que edad tienes?: "))

if edad < 14:
    print("Puedes beber agua")
elif edad >= 14 and edad < 18:
    print("Puedes beber agua y Clipper de fresa")
elif edad < 21:
    print("Puedes beber agua, Clipper de fresa y tropical")
else:
    print('Puedes beber agua, Clipper de fresa, tropical y whisky')


# Iteration 8 / What_is_in_the_center



palabra = input("Palabra para entregar el centro: ")

centro = len(palabra)//2

if len(palabra) % 2 != 0:

    print(f"{palabra} -- {palabra[centro]}")

else:

    print(f"{palabra} -- {palabra[centro-1:centro+1]}")



# Iteration 9 / Counting chars



frase = input("Escribe una frase > ").lower()

contador_a = 0

for i in frase:

    if i == 'a':

        contador_a += 1

print(f"Tiene {contador_a} a")



# Iteration 10 / Sum_of_Digits



numero_contar = input("Escribe un numero para contar sus digitos: ")

suma_total = 0

for digito in numero_contar:

    suma_total = suma_total + int(digito)

print (f"Suma total = {suma_total}")



# Bonus 1 - Reverse_String



palabra_origen = input("Introduce palabra para imprimir alreves: ")



longitud = len(palabra_origen)

palabra_reverse =""



while longitud >0:

    palabra_reverse = palabra_reverse + palabra_origen[longitud-1]

    longitud -=1

print(palabra_reverse)



# BONUS 2 - Palindromes



palindromo = input("Introduce palabra palindromo: ").lower().strip()



# primera manera: dar la vuelta a la palabra e igualar ambas palabras



if palindromo == palindromo[::-1]:

    print(f"La palabra {palindromo} ES palindromo")

else:

    print(f"la palabra {palindromo} NO es palindromo")



# segunda manera es comparar digito a digito



longitud_palindromo = len(palindromo)

contador = 0

while longitud_palindromo >0:

    if palindromo[contador] != palindromo[longitud_palindromo-1]:

        print(f"la palabra {palindromo} NO es palindromo")

        break

    longitud_palindromo -=1

    contador += 1

if longitud_palindromo == 0:

    print(f"la palabra {palindromo} ES palindromo")



# tercera manera es darle la vuelta a la palabra digito a digito y luego comparar



longitud_palindromo = len(palindromo)

palabra_alreves =""

while longitud_palindromo >0:

    palabra_alreves = palabra_alreves + palindromo[longitud_palindromo-1]

    longitud_palindromo -= 1

if palindromo == palabra_alreves:

    print("ES palindromo")

else:

    print("No es palindromo")



# BONUS 3 - The_calculator



operador = input("Que operacion quieres hacer?: ").lower().strip()

primer_numero = int(input("Introduce el primer numero: "))

segundo_numero = int(input("Introduce el segundo numero: "))

operacion = 0

if operador == "suma":

    operacion = primer_numero + segundo_numero

elif operador == "resta":

    operacion = primer_numero - segundo_numero

elif operador == "division":

    operacion = primer_numero // segundo_numero

elif operador == "multiplicacion":

    operacion = primer_numero * segundo_numero



print(f"El resultado de la {operador} de {primer_numero} y {segundo_numero} es {operacion}")

