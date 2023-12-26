FROM python:3

ADD cron.py .
ADD conn_to_BD.py .


RUN pip install mysql.connector

COPY * /

CMD [ "python", "./cron.py" ]