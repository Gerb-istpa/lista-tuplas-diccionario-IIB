# Crear diccionarios 
estudiantes = {
    "nombre"   : "Maria Eugenia",
    "edad"     : 35,
    "carrera"  : "Enfermera",
    "promedio" : 15.9    
}
# Acceso por clave 
print(estudiantes["nombre"]) 
# Acceso por get
print(estudiantes.get("edad")) 
print(estudiantes.get("telefono", "No disponible"))