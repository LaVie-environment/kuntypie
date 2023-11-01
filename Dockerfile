FROM python:3
ADD app.py /app.py
ENTRYPOINT ["python", "app.py"]