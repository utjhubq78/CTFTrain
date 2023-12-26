FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install socket
RUN pip install multiprocessing

ADD socket_server_user.py .
ADD conn_to_BD.py .

CMD [ "python", "./socket_server_user.py" ]