FROM python:3

ADD cron.py .
ADD conn_to_BD.py .


RUN pip3 install mysql.connector

COPY * /

CMD [ "python", "./cron.py" ]
