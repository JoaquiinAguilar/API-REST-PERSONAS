# API-REST-PERSONAS
Una API REST sencilla que permita crear, leer, actualizar y eliminar (CRUD) personas en una base de datos.

## Funcionalidades

- Endpoints para registrar y consultar personas.
- Búsqueda y filtrado de personas por nombre o categoría.
- Panel de administración con interfaz en HTML, CSS y JavaScript.
- Registro de datos generales de la persona, incluida fotografía y huella biométrica; la captura se divide en diferentes ventanas
  con validaciones y mensajes al usuario según el avance.
- Búsqueda de coincidencias entre huellas digitales mediante el script `fingerprint_search.py`.

## Uso del script de huellas

El archivo `fingerprint_search.py` permite comparar dos imágenes de huellas digitales y devuelve un mensaje indicando si existe coincidencia. Requiere imágenes en escala de grises.

```bash
python fingerprint_search.py referencia.png muestra.png --umbral 0.3
```

El parámetro `--umbral` controla el porcentaje mínimo de coincidencia requerido para considerar que las huellas pertenecen a la misma persona.
