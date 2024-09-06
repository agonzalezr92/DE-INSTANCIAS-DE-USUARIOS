import json
import logging
from usuario import Usuario

# Configuración del logger para registrar errores en error.log
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def crear_usuario(datos):
    try:
        # Cargar los datos en un diccionario
        datos_usuario = json.loads(datos)
        
        # Asegurarse de que todos los campos necesarios están presentes
        if not all(k in datos_usuario for k in ('nombre', 'apellido', 'email', 'genero')):
            raise ValueError('Faltan datos necesarios')

        # Crear la instancia de Usuario
        usuario = Usuario(
            nombre=datos_usuario['nombre'],
            apellido=datos_usuario['apellido'],
            email=datos_usuario['email'],
            genero=datos_usuario['genero']
        )
        return usuario

    except (json.JSONDecodeError, ValueError) as e:
        # Registrar el error en error.log
        logging.error(f'Error al crear usuario: {e} - Datos: {datos}')
        return None

def main():
    usuarios = []

    try:
        with open('usuarios.txt', 'r') as archivo:
            for linea in archivo:
                usuario = crear_usuario(linea.strip())
                if usuario is not None:
                    usuarios.append(usuario)
    
    except FileNotFoundError:
        logging.error('El archivo usuarios.txt no se encuentra.')

    print(f'Número de usuarios creados: {len(usuarios)}')

if __name__ == '__main__':
    main()
