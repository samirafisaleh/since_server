
/bin/bash eval_env.sh $1
if [ $? -ne 0 ]
then
    exit 1
fi

docker stop sinceserver_container
docker rm sinceserver_container
docker run -d -p 8000:8000 \
            -e HOST='0.0.0.0:8000' \
            --name sinceserver_container since_public_api:$1 \
            wf_run_django.sh $1
