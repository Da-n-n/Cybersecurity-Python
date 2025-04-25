import string
import random

longitud = int(input("Ingresar el tamaño de la contraseña: "))

if longitud > 50:
  print("La contraseña no debe tener más de 50 caracteres.")
else:
  caracteres = string.ascii_letters + string.digits + string.punctuation
  password = "".join(random.choice(caracteres) for i in range(longitud))
  print("La nueva contraseña seguro es: " + password)
