
docker stop pgadmin
docker rm pgadmin
docker image prune --force

docker run -d \
    -e "PGADMIN_DEFAULT_EMAIL=university.of.all.sam@gmail.com" \
    -e "PGADMIN_DEFAULT_PASSWORD=admin" \
    -p 5051:80 \
    --name pgadmin dpage/pgadmin4

