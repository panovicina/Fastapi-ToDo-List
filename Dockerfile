FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

COPY requirements.txt .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["./entrypoint.sh"]