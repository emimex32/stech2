BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

print(BLUE + "bienvenido")
edad =  int(input(GREEN + "que edad tienes? "))

if edad >= 18:
    print(YELLOW + "Eres mayor de edad")


else:
    print(YELLOW + "Eres menor de edad")

nombre = input(GREEN + "cual es tu nombre? ")
print(YELLOW + "bonito nombre")

sexo = input(GREEN + "eres hombre o mujer? ")
sexo1 = str(YELLOW + "hombre")
sexo2 = str(YELLOW + "mujer")


if sexo == sexo1:
    print(YELLOW +"eres hombre")

elif sexo == sexo2:
    print(YELLOW + "eres mujer")

else:
    print(YELLOW + "de acuerdo")

input(GREEN + "ingrese su correo electronico: ")
input(YELLOW + "contraseña: ")

input(GREEN + "como quiere que lo llamen: ")
 
print(BLUE + "proceso completado disfrute su estancia en xvideos")