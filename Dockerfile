FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get upgrade -y && apt-get install -y gcc
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV FIREBASE_KEY_PATH=firebase_key.json
COPY app app/


EXPOSE 8080

CMD ["python", "app/server.py", "serve"]
