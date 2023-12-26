docker run --name MBDt -e MYSQL_ROOT_PASSWORD=passw -e LANG=C.UTF-8 -p 3306:3306 -d mysql/mysql-server:latest
docker exec -i MBDt mysql -uroot -ppassw < BD_for_CTF2.sql