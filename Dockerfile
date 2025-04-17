FROM python:3.9-slim-bullseye

RUN apt-get update && apt-get upgrade -y && apt-get install -y gcc
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app app/

RUN python app/server.py

EXPOSE 8080

CMD ["python", "app/server.py", "serve"]
