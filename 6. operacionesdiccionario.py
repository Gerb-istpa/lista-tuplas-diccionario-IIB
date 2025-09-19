# DICCIONARIOS EN PYTHON 

# 1. CREAR EL DICCIONARIO ESTUDIANTE 
estudiante = {
    "nombre": "Maria Garcia",
    "edad": 22,
    "carrera": "Sistemas"
}

print("Diccionario original:")
print(estudiante)
print()

# 2. Modificar valores
estudiante["promedio"] = 17.2
estudiante["telefono"] = "987654321"

print("Después de agregar promedio y teléfono:")
print(estudiante)
print()

# 3. Eliminar elementos del diccionario
telefono = estudiante.pop("telefono", "No encontrado")
print(f"Teléfono eliminado: {telefono}")
print(f"Diccionario después de eliminar teléfono: {estudiante}")
print()

# 4. Métodos útiles de diccionarios
print("=== MÉTODOS DE DICCIONARIOS ===")