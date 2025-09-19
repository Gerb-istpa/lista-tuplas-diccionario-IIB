# Crear tuplas 
coordenadas=(10.5,30)
persona = ("Juan", "Pérez", 25, "Ingeniero")
colores = ("rojo", "verde", "azul")
# Acceso a elementos 
print(coordenadas[0]) 
#10
print(persona[1]) 
#Pérez

# Desempaquetado(dividir) de tuplas
x,y = coordenadas 
nombre, apellido, edad, profesion = persona
print(f"Coordenada X: {x}, Y: {y}")
print(f"hola  {nombre} {apellido}  bienvenido a la clase, se que eres {profesion} y tienes {edad} años")