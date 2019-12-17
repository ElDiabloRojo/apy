FROM python:3

LABEL maintainer="ElDiabloRojo <holdens.uk@googlemail.com>"
LABEL version="1.3"
LABEL description="Docker image for apy."

ENV BOKEH_RESOURCES=inline

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY . app/

WORKDIR /app

ENTRYPOINT [ "gunicorn" ]
CMD [ "--workers", "2", "--threads", "4", "--log-level", "info", "--bind", "0.0.0.0:5000", "run:app" ]