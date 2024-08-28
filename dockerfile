FROM python:3.11-slim-buster

WORKDIR /Technical_Habi

COPY . /Technical_Habi

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [ "python", "main.py" ]
