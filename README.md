## Flask_Emulator

Flask_Emulator es una aplicación web desarrollada con Flask, un framework de Python para construir aplicaciones web dinámicas. Esta aplicación permite jugar a juegos emulados directamente desde la misma página web, sin necesidad de descargar ningún software adicional. Esto ofrece una experiencia de usuario conveniente y portátil, eliminando la necesidad de configuraciones complicadas o instalaciones tediosas.

### Requisitos

Para ejecutar Flask_Emulator en tu máquina local, necesitarás:

- Python 3.x instalado en tu sistema.
- El paquete Flask, que puedes instalar fácilmente a través de pip, el gestor de paquetes de Python.

### Instalación

Sigue estos pasos para configurar Flask_Emulator en tu entorno local:

1. Clona este repositorio en tu máquina local usando el comando `git clone`.
2. Navega hasta el directorio del proyecto y ejecuta el siguiente comando para instalar las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

### Uso

Una vez que hayas instalado las dependencias, puedes ejecutar la aplicación Flask_Emulator con el siguiente comando:

```bash
python app.py
```

En el futuro cuando la aplicación este hosteada en un servidor y tengamos configurado un DNS para acceder a la aplicación, simplemente abre tu navegador y navega hasta la URL proporcionada. Por el momento, puedes acceder a la aplicación localmente en http://localhost:5000.

### Configuración

No se requiere ninguna configuración adicional para ejecutar Flask_Emulator en tu máquina local. La aplicación viene preconfigurada con valores predeterminados que funcionarán fuera de la caja.

### Contribuciones

Si estás interesado en contribuir al desarrollo de Flask_Emulator, te invitamos a seguir estos pasos:

1. Realiza un fork del repositorio en GitHub.
2. Crea una nueva rama para tu contribución utilizando el formato `feature/nueva-caracteristica`.
3. Realiza tus cambios y haz un commit de tus modificaciones con un mensaje descriptivo.
4. Sube tus cambios a tu repositorio fork en GitHub.
5. Crea una solicitud de extracción (pull request) para que tus cambios sean revisados e integrados en el repositorio principal.

### Dockerización

Flask_Emulator está dockerizado para facilitar su despliegue y gestión. Al contener la aplicación en un contenedor Docker, se garantiza un entorno de ejecución consistente independientemente del sistema operativo o las configuraciones locales del host. Además, la dockerización permite una fácil escalabilidad y distribución de la aplicación en diferentes entornos de desarrollo, prueba y producción.

--- 