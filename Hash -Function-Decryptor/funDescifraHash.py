import hashlib

hash_file = "00d85c2b3a9529b229108210a600cec374835394e4b2b64aaad1b16491dee9c4"

dic_file = input("Ingrese la dirección del archivo del diccionario: ")

with open(dic_file, 'r') as file:
  
  diccionario = [line.strip() for line in file]
  
  for password in diccionario:
    
    hash_calculado = hashlib.sha256(password.encode()).hexdigest()
    
    if hash_calculado == hash_file:
      print("La contraseña original es: " + password)
      break
    else:
      print("La contraseña no se encuentra en el diccionario")