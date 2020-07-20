FROM python:3.8-slim

WORKDIR /csvify

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app/ .

CMD ["python", "csvify.py"]

