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
# Obtener solo las claves (keys)
print("Claves del diccionario:")
print(list(estudiante.keys()))

# Obtener solo los valores (values)
print("Valores del diccionario:")
print(list(estudiante.values()))

# Obtener pares clave-valor (items)
print("Pares clave-valor:")
print(list(estudiante.items()))
print()

# 5. Verificar si existe una clave
if "nombre" in estudiante:
    print("El estudiante tiene nombre registrado")
    print(f"Nombre: {estudiante['nombre']}")
else:
    print("No hay nombre registrado")
    
    
    
if "email" in estudiante:
    print("El estudiante tiene nombre registrado")
    print(f"Nombre: {estudiante['email']}")
else:
    print("No hay email registrado")
    
# 6. Usar get() para evitar errores
telefono = estudiante.get("telefono", "No tiene teléfono")
print(f"Teléfono: {telefono}")

# 7. EJEMPLO COMPLETO - Varios estudiantes
print("\n=== EJEMPLO CON MÚLTIPLES ESTUDIANTES ===")
# Lista de diccionarios
estudiantes = [
    {"nombre": "Ana", "edad": 20, "promedio": 18.5},
    {"nombre": "Carlos", "edad": 19, "promedio": 16.8},
    {"nombre": "María", "edad": 21, "promedio": 9.25},
    {"nombre": "Mario", "edad": 31, "promedio": 9.2},
    {"nombre": "Ericks", "edad": 42, "promedio": 15.5},
    {"nombre": "Jossi", "edad": 55, "promedio": 19.2}
]
print("Lista de estudiantes:")
for i, est in enumerate(estudiantes):
    print(f"{i+1}. {est['nombre']} - {est['edad']}- {est['promedio']}  ")
    
    
# 8. Encontrar el mejor estudiante
mejor_estudiante=max(estudiantes,key=lambda mejorNota:mejorNota['promedio'])
print(f"el mejor alumno(a) es :  {mejor_estudiante['nombre']} con promdio de {mejor_estudiante['promedio']}")

# 9. EJERCICIO PRÁCTICO - Agenda de contactos
print("\n=== AGENDA DE CONTACTOS ===")

agenda = {
    "mamá": "123-456-789",
    "papá": "987-654-321", 
    "hermana": "456-789-123",
    "mejor_amigo": "789-123-456"
}

# Buscar un contacto
contacto_buscar="mamá"

if contacto_buscar in agenda:
    print(f"El telefono del contacto {contacto_buscar} es {agenda[contacto_buscar]}")

# Agregar nuevo contacto
agenda["abuela"] = "321-654-987"
print(f"Contactos en la agenda: {len(agenda)}")

# Mostrar todos los contactos
print("Todos los contactos:")
for nombre, telefono in agenda.items():
    print(f"📞 {nombre}: {telefono}")