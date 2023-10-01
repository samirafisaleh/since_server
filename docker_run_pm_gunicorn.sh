
/bin/bash eval_env.sh $1
if [ $? -ne 0 ]
then
    exit 1
fi

dir_name=${PWD##*/}
cont_name="${dir_name}_container"
port=8000

docker stop $cont_name
docker rm $cont_name
docker run -d -p $port:$port \
            -e HOST="0.0.0.0:${port}" \
            --name $cont_name $dir_name:$1 \
            gunicorn_run.sh $1
