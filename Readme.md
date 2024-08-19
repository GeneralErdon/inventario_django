El presente proyecto es para la demostración de la prueba técnica de Django Rest Framework de un sistema de inventario básico

# Tabla de contenidos

| Contenido                 | Link                        |
| ------------------------- | --------------------------- |
| Requisitos de instalación | [Requisitos](#Requisitos)   |
| Instalación               | [Instalacion](#Instalación) |
| Ejecutar Tests            | ...                         |
| Probar endpoints          | ...                         |

---

# Requisitos

| Nombre                           | Version          |
| -------------------------------- | ---------------- |
| Python                           | 3.11             |
| Docker (opcional)                | 27.1.2 (lastest) |
| Docker-compose (plugin opcional) | 2.29.1 (lastest) |

> [!TIP] 
> Para la descarga de los requisitos puede ayudarse de los siguientes enlaces: [Docker](https://docs.docker.com/engine/install) [Docker Linux Post-Install](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) [Python (Windows)](https://www.python.org/downloads/release/python-3119/)
> Para descargar python en Linux utilizar el respectivo comando del manager de instalación de la distribución.
>  Fedora: `sudo dnf install python3.11`
>  Arch Linux: `sudo pacman -S python3.11`
>  Ubuntu o Debian based distro: `sudo apt install python3.11`


> [!TIP] 
> Para visualizar su versión de cada requisito puede ejecutar los siguientes comandos: 
> Python: `python --version` o `python3 --version` o `python3.11 --version` (en caso de tener varias versiones instaladas)
> Docker: `docker --version`
> Docker Compose: `docker compose version`

---
# Instalación
### Descarga del repositorio
Primero se debe clonar el repositorio en un directorio, puedes ejecutar el siguiente comando en tu terminal
```bash
git clone https://github.com/GeneralErdon/inventario_django.git
```

> [!NOTE]
> El comando traerá el repositorio en un directorio con el mismo nombre, si deseas clonarlo dentro de otro directorio agrega la ruta del directorio al final del comando

### Instalación manual (sin docker)
Primero que nada hay que descargar las dependencias y paquetes necesarios para que funcione

1. Entrar en el directorio utilizando la terminal
```bash
cd inventario_django
```
2. Crear el entorno virtual de python con el comando:
```bash
python3.11 -m venv env 
```
3. Activar el entorno virtual de python 
```sh 
source env/bin/activate 
```
4. Instalar las dependencias listadas en el requirements.txt
```sh 
pip install -r requirements.txt 
```
5. Realizar la configuración inicial de las variables de entorno, en el directorio del proyecto  hay un archivo llamado  **example.env**, haz un archivo .env usandolo como plantilla, puedes utilizar el comando a continuación para hacer una copia
```sh 
cat example.env > .env
```

> [!IMPORTANT] 
> Es importante que el archivo de las variables de entorno se encuentre en el directorio raíz del proyecto y que tenga el nombre de ".env"

6. Crear la base de datos del servicio, se debe acceder a postgreSQL y crear una base de datos con el mismo nombre que se encuentre en el ".env" del proyecto en la llave "POSTGRES_DB" 

```PostgreSQL
CREATE DATABASE inventory_db WITH OWNER [Insertar aca USERNAME]
```

> [!TIP] 
> Otra opción para la base de datos es instanciarla en Docker con el simple comando de 
> ``` bash
> docker compose up -d inventory_db
> ```
> Y cambiar la configuración de POSTGRES_PORT a la 5433 (colocado así para que no haga conflicto con el postgres que esté instalado nativo en el equipo)


7. ejecutar las migraciones de Django una vez ya se haya configurado el usuario y contraseña en el archivo **".env"** en las llaves POSTGRES_PASSWORD y POSTGRES_USER, las migraciones crearán las tablas y relaciones correspondientes.
```bash
python manage.py migrate
```

> [!TIP] 
> Por defecto al realizar la primera migración se creará un super usuario por defecto con las credenciales de username: admin, password: admin

8. Ahora se puede iniciar el programa con el comando del servidor integrado de Django
```bash
python manage.py runserver
```

### Instalación con Docker (recomendado)
1. Realizar la configuración inicial de las variables de entorno, en el directorio del proyecto  hay un archivo llamado  **example.env**, haz un archivo .env usandolo como plantilla, puedes utilizar el comando a continuación para hacer una copia
```sh 
cat example.env > .env
```

> [!IMPORTANT] 
> Es importante que el archivo de las variables de entorno se encuentre en el directorio raíz del proyecto y que tenga el nombre de ".env"

2. Ejecutar el siguiente comando para montar todas las imágenes 
```sh
docker compose up -d
```
3. Esperar que se terminen de crear las imágenes y ya estarán funcionales, el enrutador (Nginx) estará montado por defecto para `localhost:4000` a partir de allí se podrán ejecutar las peticiones.

---
