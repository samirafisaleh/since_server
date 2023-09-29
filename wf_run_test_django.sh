
/bin/bash eval_env.sh $1
if [ $? -ne 0 ]
then
    exit 1
fi

cd source/project/
python manage.py test -v 2 --settings=settings.settings_$1