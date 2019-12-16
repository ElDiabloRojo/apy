FROM python:3

LABEL maintainer="ElDiabloRojo <holdens.uk@googlemail.com>"
LABEL version="1.0"
LABEL description="Docker image for apy.""

ADD app/ app/

RUN pip install -r app/requirements.txt

WORKDIR /app

ENTRYPOINT [ "gunicorn" ]
CMD [ "-w", "4", "--bind", "0.0.0.0:5000", "run:app" ]