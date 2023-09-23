
if [[ $# -eq 0 ]];
then
    echo "FATAL: No environment arguments supplied."
    echo "INFO: Exiting ...."
    exit 1
fi

if [ "$1" != "dev" -a "$1" != "test" -a "$1" != "stage" -a "$1" != "prod" ]
then
    echo "FATAL: Invalid environment: Choices: dev, test, stage, prod"
    echo "INFO: Exiting ...."
    exit 1
fi

echo "Environment: $1"

docker stop sinceserver_container
docker rm sinceserver_container
docker run -d -p 8000:8000 \
            -e HOST='0.0.0.0:8000' \
            --name sinceserver_container since_public_api:$1 \
            gunicorn_run.sh $1
