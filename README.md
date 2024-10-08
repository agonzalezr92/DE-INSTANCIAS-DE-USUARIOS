# Proyecto de Gestión de Usuarios en Python

Este proyecto consiste en una aplicación en consola en Python que gestiona la creación de instancias de usuarios a partir de datos almacenados en un archivo de texto. La aplicación lee los datos en formato JSON, crea instancias de la clase `Usuario`, y maneja posibles errores durante este proceso.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos principales:

- **`usuario.py`**: Define la clase `Usuario` que encapsula la información del usuario, incluyendo nombre, apellido, correo electrónico y género.

- **`usuarios.txt`**: Contiene los datos de los usuarios en formato JSON. Cada línea representa un usuario con sus atributos.

- **`script.py`**: Archivo principal que lee el archivo `usuarios.txt`, crea instancias de `Usuario`, y maneja posibles excepciones, registrando errores en un archivo `error.log`.

## Instalación y Requisitos

Este proyecto está escrito en Python 3. Asegúrate de tener Python 3 instalado en tu sistema.

1. Clona el repositorio (si está disponible en un repositorio remoto) o descarga los archivos `usuario.py`, `usuarios.txt`, y `script.py` a tu directorio local.

2. Instala Python 3 (si aún no lo tienes). Puedes descargarlo desde [python.org](https://www.python.org/).

3. No se requieren dependencias adicionales para ejecutar el proyecto.

## Uso de la Aplicación

### Ejecutar el Script

1. Coloca el archivo `usuarios.txt` en el mismo directorio que `script.py` y `usuario.py`.

2. Ejecuta el script `script.py` desde la línea de comandos:

   ```bash
   python script.py
   ```

3. El script procesará cada línea del archivo `usuarios.txt`, intentará crear una instancia de `Usuario` con los datos proporcionados, y almacenará las instancias en una lista. Si se produce un error, este será registrado en el archivo `error.log`.

### Estructura de Datos en `usuarios.txt`

Cada línea del archivo `usuarios.txt` debe estar en formato JSON y debe contener los siguientes campos:

- `nombre`: Nombre del usuario.
- `apellido`: Apellido del usuario.
- `email`: Correo electrónico del usuario.
- `genero`: Género del usuario.

Ejemplo de una línea en `usuarios.txt`:

```json
{"nombre": "Page", "apellido": "Stappard", "email": "pstappard0@java.com", "genero": "Bigender"}
```

## Detalles de Implementación

- **Encapsulamiento**: La clase `Usuario` encapsula la información del usuario y proporciona métodos para manipular estos datos.

- **Manejo de Errores**: El script maneja excepciones durante la lectura del archivo y la creación de instancias. Los errores se registran en `error.log` para su posterior revisión.

## Autores

- Arlenis Gonzalez
- Karen Limari
- Ambar Zambrano


## Contribuciones

Las contribuciones al proyecto son bienvenidas. Si tienes alguna sugerencia o encuentras algún error, por favor, abre un issue en el repositorio (si está disponible) o contacta con el mantenedor del proyecto.

## Licencia

Este proyecto está licenciado bajo la MIT License - consulta el archivo `LICENSE` para más detalles.

---
