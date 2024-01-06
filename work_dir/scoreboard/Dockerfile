FROM python:3

RUN mkdir -p ./templates

ADD scoreboard.py .
ADD index.html ./templates

RUN pip install flask
RUN pip install mysql.connector

COPY * /

CMD [ "python", "./scoreboard.py" ]