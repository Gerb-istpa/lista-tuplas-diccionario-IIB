# ===============================================
# EJERCICIOS COMPLETOS: LISTAS Y TUPLAS EN PYTHON
# ===============================================

print("🐍 PYTHON PARA PRINCIPIANTES -  TUPLAS 🐍")
print("=" * 50)
# ===============================================
# 📷 PARTE 2: TUPLAS
# ===============================================
print("\n\n📷 TRABAJANDO CON TUPLAS")
print("-" * 30)
# 1. CREAR TUPLAS
print("1. Creando tuplas:")
coordenadas = (10.5, 20.3)
print(f"Coordenadas: {coordenadas}")

fecha_nacimiento = (15, "marzo", 1990)
print(f"Fecha de nacimiento: {fecha_nacimiento}")

# Tupla de un solo elemento (¡cuidado con la coma!)
un_elemento = (42,)
print(f"Tupla de un elemento: {un_elemento}")

# 2. ACCEDER A ELEMENTOS DE TUPLAS
print("\n2. Accediendo a elementos:")
colores_rgb = (255, 128, 0)
print(f"Color RGB: {colores_rgb}")
print(f"Rojo: {colores_rgb[0]}")
print(f"Verde: {colores_rgb[1]}")
print(f"Azul: {colores_rgb[2]}")

# 3. DESEMPAQUETADO DE TUPLAS
print("\n3. Desempaquetado de tuplas:")
punto = (100, 200)
x, y = punto  # Desempaquetar
print(f"Coordenada X: {x}")
print(f"Coordenada Y: {y}")

# Desempaquetado con más elementos
persona = ("María", 25, "Ingeniera", "Soltera")
nombre, edad, profesion, estado_civil = persona
print(f"Nombre: {nombre}, Edad: {edad}, Profesión: {profesion}, estado civil: {estado_civil}")

# 4. TUPLAS SON INMUTABLES
print("\n4. Las tuplas NO se pueden cambiar:")
datos_fijos = ("DNI", "123456789", "Perú")
print(f"Datos fijos: {datos_fijos}")
print("❌ No podemos hacer: datos_fijos[1] = '87654321'")
print("✅ Las tuplas protegen los datos importantes")

# 5. MÉTODOS DE TUPLAS (LIMITADOS)
print("\n5. Métodos disponibles en tuplas:")
numeros_tupla = (1, 2, 3, 2, 4, 2, 5)
print(f"Tupla de números: {numeros_tupla}")
print(f"Contar el número 2: {numeros_tupla.count(2)}")
print(f"Posición del número 3: {numeros_tupla.index(3)}")
print(f"Longitud de la tupla: {len(numeros_tupla)}")

# 6. RECORRER TUPLAS
print("\n6. Recorriendo tuplas:")
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
print("Días de trabajo:")
for i, dia in enumerate(dias_semana):
    print(f"{i+1}. {dia}")

# 7. TUPLAS ANIDADAS
print("\n7. Tuplas anidadas:")
estudiante_completo = (
    "Carlos López",
    (8.5, 9.0, 7.5, 8.2),  # Notas (tupla dentro de tupla)
    ("Matemáticas", "Física", "Química","LP")  # Materias
)
nombre_est = estudiante_completo[0]
notas = estudiante_completo[1]
materias = estudiante_completo[2]
print(f"Estudiante: {nombre_est}")
print(f"Notas: {notas}")
print(f"Promedio: {sum(notas) / len(notas):.2f}")