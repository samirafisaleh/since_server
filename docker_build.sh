
/bin/bash eval_env.sh $1
if [ $? -ne 0 ]
then
    exit 1
fi

docker build --build-arg env=$1 --tag since_public_api:$1 .