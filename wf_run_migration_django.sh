
/bin/bash eval_env.sh $1
if [ $? -ne 0 ]
then
    exit 1
fi

cd source/project/
set -a
export DJANGO_SETTINGS_MODULE=settings.settings
export DJANGO_ENV=$1
set +a
python manage.py makemigrations --settings=settings.settings
python manage.py migrate --settings=settings.settings