
docker stop postgresql
docker rm postgresql
docker image prune --force

docker run -itd \
    -e POSTGRES_USER=admin \
    -e POSTGRES_PASSWORD=my_password \
    -p 5432:5432 \
    --name postgresql postgres