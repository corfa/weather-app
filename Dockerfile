FROM python:3.11-slim-buster

RUN pip install uv

WORKDIR /opt

COPY app/ ./
COPY entrypoint.sh entrypoint.sh

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/opt/entrypoint.sh"]
