# Crear listas 
frutas=["manzana","mango","mandarina","platano","lucuma"] #lista en string
numeros = [10, 25, 30, 45, 50]  #lista numero enteros
decimales = [3.14, 2.71, 1.61] #lista numero decimales|
mixta = ["Juan", 25, True, 3.14]
# Acceso por índice (comienza en 0)
print( "Posicion 2 es :",frutas[2]) #forma clasica
print(f"la posicion 2 es : {frutas[2]}") #forma moderna llamado template o fstring
print(frutas[-1])
print(frutas[-4])
# naranja (último elemento) 
# Acceso por rango (slicing)
print(frutas[1:4])