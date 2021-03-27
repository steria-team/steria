FROM python:3.7.7-alpine

RUN adduser -D steria

WORKDIR /home/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && pip install gunicorn

#install gunicorn

COPY steria steriaserver

COPY steria.py .

ENV FLASK_APP api.py

RUN chown -R steria:steria ./

USER steria

#EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["steria.py"]
