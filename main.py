import random
import string

longitud = int(input("¿Cuántos caracteres quieres que tenga la contraseña? "))

caracteres = string.ascii_letters + string.digits + string.punctuation

contraseña = ""

for i in range(longitud):
    contraseña += random.choice(caracteres)

print("Tu contraseña es:", contraseña)