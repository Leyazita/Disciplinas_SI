# Use uma imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo do servidor para o container
COPY server.py .

# Execute o servidor quando o container for iniciado
CMD ["python", "server.py"]
