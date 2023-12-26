FROM python:3

ADD scoreboard.py .

RUN pip install flask
RUN pip install mysql.connector

COPY * /

CMD [ "python", "./scoreboard.py" ]