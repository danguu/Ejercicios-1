def mcd(a, b):
  
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
 
    return (a * b) // mcd(a, b)

# Prueba 
a = 12
b = 18
print(f"El MCD de {a} y {b} es: {mcd(a, b)}")
print(f"El MCM de {a} y {b} es: {mcm(a, b)}")