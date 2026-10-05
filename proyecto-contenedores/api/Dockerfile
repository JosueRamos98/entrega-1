FROM python:3.12-alpine

LABEL proyecto="entrega2-devops" \
      servicio="api" \
      descripcion="Logica de negocio, expone /status y /health"

WORKDIR /app

# Las dependencias se instalan antes de copiar el codigo para
# aprovechar la cache de capas de Docker: si solo cambia app.py,
# esta capa no se vuelve a construir.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# El proceso no corre como root dentro del contenedor
RUN adduser -D -u 10001 apiuser
USER apiuser

EXPOSE 5000

CMD gunicorn --bind 0.0.0.0:5000 --workers 2 app:app
