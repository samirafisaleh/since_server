
/bin/bash eval_env.sh $1
if [ $? -ne 0 ]
then
    exit 1
fi

set -a
export DJANGO_SETTINGS_MODULE=settings.settings_$1
set +a
pushd source/project/
gunicorn -c settings/gunicorn_config_$1.py project.wsgi