
/bin/bash eval_env.sh $1
if [ $? -ne 0 ]
then
    exit 1
fi

cd source/project/
python manage.py makemigrations --settings=settings.settings_$1
python manage.py migrate --settings=settings.settings_$1