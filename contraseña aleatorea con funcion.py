import random

def gen_pass(pass_length):
    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    resultado = ""
    for i in range(pass_length):
        resultado += random.choice(caracteres)
    return resultado

# Solicitar longitud de la contraseña al usuario
longitud = int(input("Ingresa tu longitud de contraseña: "))
# Generar la contraseña
password = gen_pass(longitud)
# Imprimir la contraseña generada
print(f"Tu contraseña con longitud {longitud} es: {password}")
