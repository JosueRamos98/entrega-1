FROM nginx:1.27-alpine

LABEL proyecto="entrega2-devops" \
      servicio="web" \
      descripcion="Capa de presentacion y proxy inverso hacia la API"

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY html/ /usr/share/nginx/html/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD wget -q -O /dev/null http://127.0.0.1/ || exit 1
