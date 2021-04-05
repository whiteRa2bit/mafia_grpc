FROM python:3.8

RUN mkdir /app/
WORKDIR /app/
COPY requirements.txt .

RUN apt-get update

RUN pip install -r requirements.txt

COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["/bin/bash"]