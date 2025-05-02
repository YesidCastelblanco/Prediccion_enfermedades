# Guía para Ejecutar una Imagen Docker y Visualizar la Web

Este documento describe los pasos para instalar Docker, construir una imagen, ejecutar un contenedor y acceder a una página web desplegada en un contenedor Docker.

## 1. Instalación de Docker

### 1.1. Requisitos previos
Antes de comenzar, asegúrate de tener los siguientes requisitos:

- Un sistema operativo compatible (Windows, macOS o Linux).
- Privilegios de administrador o sudo en tu máquina.

### 1.2. Instalación en Windows

1. Dirígete a la página oficial de instalación de Docker:  
   [Docker Desktop para Windows](https://www.docker.com/products/docker-desktop).
   
2. Descarga el instalador y sigue las instrucciones. Durante la instalación, asegúrate de habilitar la opción "WSL 2" si estás usando Windows 10/11.

3. Una vez finalizada la instalación, abre Docker Desktop y espera a que se inicie correctamente.

### 1.3. Instalación en macOS

1. Dirígete a la página oficial de instalación de Docker:  
   [Docker Desktop para macOS](https://www.docker.com/products/docker-desktop).

2. Descarga el archivo `.dmg` y sigue las instrucciones en pantalla para instalar Docker.

3. Abre Docker desde la carpeta de Aplicaciones y espera a que se inicie.

### 1.4. Instalación en Linux

1. Abre una terminal y ejecuta los siguientes comandos:

```bash
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce
```

2. Verifica que Docker se haya instalado correctamente ejecutando:

```bash
sudo docker --version
```
 
## 2. Crear y Construir una Imagen Docker

### 2.1. Prepara el Dockerfile

1. Crea un archivo llamado `Dockerfile` en el directorio de tu proyecto. Este archivo debe contener la configuración para tu imagen Docker. Un ejemplo básico para una aplicación web en Python (usando Flask, por ejemplo) es el siguiente:

```Dockerfile
# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto 5000
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
```

Para este caso, ya tenemos adjunto el archivo Dockerfile con la siguiente información:

```
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]
```

### 2.2. En nuestro ordenador, debemos crear una carpeta con el nombre: mlops_enfermedades ,la cual debe contener los siguientes archivos:

* Dockerfile
* app.py
* predictor.py
* Dentro de la carpeta mlops_enfermedades creamos una carpeta con el nombre templates y dentro de esta carpeta agregamos el archivo 
  index.html.

  Teniendo en cuenta lo anterior, nos aseguramos que la carpeta mlops_enfermedades quede con los siguientes objetos:
* Dockerfile
* app.py
* predictor.py
* templates
  
### 2.3. Construir la Imagen Docker

1. Navega al directorio donde tienes el `Dockerfile` por CMD y ejecuta el siguiente comando en la terminal para construir la imagen:

```bash
docker build -t mlops_enfermedades .
```

Este comando creará una imagen Docker llamada mlops_enfermedades . usando el Dockerfile en el directorio actual (`.`).

---

## 3. Ejecutar el Contenedor Docker

### 3.1. Ejecuta el Contenedor

1. Una vez que la imagen se haya creado correctamente, puedes ejecutar un contenedor basado en esa imagen usando el siguiente comando:

```bash
docker run -d -p 5000:5000 mlops_enfermedades
```

Aquí:
- `-d` ejecuta el contenedor en segundo plano.
- `-p 5000:5000` mapea el puerto 5000 del contenedor al puerto 5000 de tu máquina local (si usas otro puerto, ajústalo).
- `mlops_enfermedades` es el nombre de la imagen que creaste.

### 3.2. Verifica que el Contenedor se Esté Ejecutando

1. Para verificar que el contenedor está corriendo, puedes usar el siguiente comando:

```bash
docker ps
```

Este comando te mostrará los contenedores en ejecución, junto con los puertos expuestos.

---

## 4. Acceder a la Página Web

1. Abre tu navegador web y visita la siguiente URL:

```
http://localhost:5000
```

Deberías ver la página de tu aplicación web. Si todo está bien configurado, deberías ver la página web con los 3 campos de sintomas y listo para predecir.

---

## 5. Detener el Contenedor

1. Si deseas detener el contenedor, primero debes encontrar el ID del contenedor:

```bash
docker ps
```

2. Luego, usa el siguiente comando para detener el contenedor:

```bash
docker stop <ID del contenedor>
```

---

## 6. Eliminar la Imagen y Contenedores

### 6.1. Eliminar el Contenedor

Para eliminar el contenedor:

```bash
docker rm <ID del contenedor>
```

### 6.2. Eliminar la Imagen

Para eliminar la imagen que creaste:

```bash
docker rmi mlops_enfermedades
```

---

## 7. Referencias

- [Instalación de Docker](https://docs.docker.com/get-docker/)
- [Documentación de Dockerfile](https://docs.docker.com/engine/reference/builder/)
- [Documentación de Docker run](https://docs.docker.com/engine/reference/commandline/run/)
