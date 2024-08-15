def factorial(n):

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Ejemplo 
numero = 5
factorial_numero = factorial(numero)
print(f"El factorial de {numero} es: {factorial_numero}")