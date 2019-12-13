FROM python:3

ADD app/ app/

RUN pip install -r app/requirements.txt

WORKDIR /app

ENTRYPOINT [ "gunicorn" ]
CMD [ "-w", "4", "--bind", "0.0.0.0:5000", "run:app" ]