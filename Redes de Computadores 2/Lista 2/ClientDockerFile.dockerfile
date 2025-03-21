# Use uma imagem base do Python
FROM python:3.8

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie o arquivo do cliente para o container
COPY client.py .

# Execute o cliente quando o container for iniciado
CMD ["python", "client.py"]
