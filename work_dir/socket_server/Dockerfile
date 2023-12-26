FROM python:3

ADD socket_server_user.py .
ADD conn_to_BD.py .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "socket_server_user.py" ]