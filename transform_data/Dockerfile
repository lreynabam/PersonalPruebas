#imagen base
FROM python:3.9-slim
#directorio de trabajo
WORKDIR /app
#archivo requirements.txt para dependencias
COPY requirements.txt .
COPY transformation_data.py .
#dependencias necesarias
RUN pip install pandas
#archivo
CMD ["python", "transformation_data.py"]
