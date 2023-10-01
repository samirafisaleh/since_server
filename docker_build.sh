
/bin/bash eval_env.sh $1
if [ $? -ne 0 ]
then
    exit 1
fi

dir_name=${PWD##*/}
docker build --build-arg env=$1 --tag $dir_name:$1 .