FROM python:3.9.10-slim-bullseye

WORKDIR /app

COPY . .

EXPOSE 5000

CMD [ "python", "main.py" ]
