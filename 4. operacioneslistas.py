# ===============================================
# EJERCICIOS COMPLETOS: LISTAS Y TUPLAS EN PYTHON
# ===============================================

print("🐍 PYTHON PARA PRINCIPIANTES - LISTAS 🐍")
print("=" * 50)

# ===============================================
# 📝 PARTE 1: LISTAS
# ===============================================
print("\n📝 TRABAJANDO CON LISTAS")
# 1. CREAR UNA LISTA DE COMPRAS
print("1. Creando lista de compras:")
compras = ["pan", "leche", "huevos", "queso"] #LISTA DE STRING
print(f"Lista original: {compras}")

# 2. AGREGAR ELEMENTOS
print("\n2. Agregando elementos:")
compras.append("mantequilla")  # Agregar al final
print(f"Después de append: {compras}")

compras.insert(1, "yogurt")    # Insertar en posición específica
print(f"Después de insert: {compras}")

# 3. ACCEDER A ELEMENTOS
print("\n3. Accediendo a elementos:")
print(f"Primer elemento: {compras[0]}")
print(f"Último elemento: {compras[-1]}")
print(f"Segundo y tercer elemento: {compras[1:3]}")

# 4. MODIFICAR ELEMENTOS
print("\n4. Modificando elementos:")
compras[0] = "Biscocho integral"
print(f"Después de cambiar el pan: {compras}")

# 5. ELIMINAR ELEMENTOS
print("\n5. Eliminando elementos:")
compras.remove("yogurt")      # Eliminar por valor
print(f"Después de remove: {compras}")

elemento_eliminado = compras.pop()  # Eliminar último
print(f"Eliminamos: {elemento_eliminado}")
print(f"Lista final: {compras}")

# 6. MÉTODOS ÚTILES DE LISTAS
print("\n6. Métodos útiles:")
numeros = [3, 1, 4, 11, 5, 9, 2, 6,25,85]
print(f"Lista de números: {numeros}")
print(f"Longitud: {len(numeros)}")
print(f"Número máximo: {max(numeros)}")
print(f"Número mínimo: {min(numeros)}")
print(f"Suma total: {sum(numeros)}")
# Contar elementos
print(f"¿Cuántas veces aparece el 1?: {numeros.count(1)}")

# Ordenar
numeros_ordenados = numeros.copy()  # Hacer una copia
numeros_ordenados.sort()
print(f"Números ordenados: {numeros_ordenados}")

# 7. RECORRER UNA LISTA
print("\n7. Recorriendo la lista:")
frutas = ["manzana", "plátano", "naranja", "fresa","pera","lucuma","shirimoya","pacay"]

print("Método 1 - Solo elementos:")
for frutita in frutas:
    print(f"🍎 {frutita}")
    
print("\nMétodo 2 - Con índice:")
#n-1
#8-1=7
for i, fruta in enumerate(frutas):
    print(f"{i+1}. {fruta}")
    
 # 8. LISTAS CON DIFERENTES TIPOS
print("\n8. Lista mixta:")
datos_persona = ["Juan", 20, True, 85.5]
print(f"Datos mixtos: {datos_persona}")
print(f"Nombre: {datos_persona[0]}")
print(f"Edad: {datos_persona[1]} años")   
print(f"Logico: {datos_persona[2]}")
print(f"Puntaje: {datos_persona[3]} puntos")  
    