# 1. Imagen base: Usamos una versión ligera de Python sobre Linux Alpine
FROM python:3.11-alpine

# 2. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiamos el archivo de dependencias e las instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiamos el resto del código de la aplicación
COPY app.py .

# 5. Exponemos el puerto donde escucha Flask
EXPOSE 5000

# 6. Comando para arrancar la aplicación
CMD ["python", "app.py"]