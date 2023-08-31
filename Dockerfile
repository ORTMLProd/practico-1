# imagen base
FROM python:3.9.6

# crea y fija directorio de trabajo
WORKDIR /scrapers

# copia todo hacia el contenedor
COPY . .

# instala las dependencias de nuestro proyecto
RUN pip install -r requirements.txt

# ejecuta bash para usar la línea de comandos
CMD ["bash"]
