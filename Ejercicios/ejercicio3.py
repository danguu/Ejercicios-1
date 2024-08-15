def sucesor(n):
 
  return n + 1

def suma(a, b):

  if b == 0:
    return a
  else:
    return sucesor(suma(a, b - 1))

def multiplicacion(a, b):

  if b == 0:
    return 0
  else:
    return suma(a, multiplicacion(a, b - 1))

# Prueba 
print(suma(5, 3))  # Salida: 8
print(multiplicacion(4, 2))  # Salida: 8