pip freeze > requirements.txt
chmod +x ./entrypoint.sh
http://0.0.0.0:8000
docker-compose up -d --build
./manage.py startapp taskapp
docker exec -it django /bin/shdocker run h

tp1.delay()

from celery import group
from newapp.tasks import tp1, tp2, tp3, tp4, tp5, task1
task_group = group(tp1.s(), tp2.s(), tp3.s(), tp4.s())
task_group.apply_async()

from celery import chain
from newapp.tasks import tp1, tp2, tp3
task_chain = chain(tp1.s(), tp2.s(), tp3.s())
task_chain.apply_async()
task_chain = chain(tp3.s(), tp2.s(), tp3.s())

# Remove all docker
docker stop $(docker ps -aq) && docker rm $(docker ps -aq) && docker rmi $(docker images -aq)