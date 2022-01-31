FROM python:3.7

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3500

CMD ["python3", "scale.py"]