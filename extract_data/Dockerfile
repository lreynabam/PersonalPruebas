#imagen base
FROM python:3.9-slim
#directorio de trabajo
WORKDIR /app
#archivo requirements.txt para dependencias
COPY requirements.txt .
COPY extract_data_to_csv.py .
#dependencias necesarias
RUN pip install pandas psycopg2-binary 
#archivo
CMD ["python", "extract_data_to_csv.py"]
