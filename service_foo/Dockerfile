FROM python:3.9-buster

LABEL org.label-schema.vendor="Pedrozena"
LABEL org.label-schema.schema-version="1.0"

ENV TZ=Etc/UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /opt/pedrozena/foo
COPY ./src ./src
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/opt/pedrozena/foo
ENTRYPOINT python src/main.py