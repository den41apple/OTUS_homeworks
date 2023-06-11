FROM python:3.9-buster

# Для корректной работы командной строки
ENV PYTHONUNBUFFERED=1

WORKDIR /homework_03

COPY ./ ./

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EXPOSE 8000