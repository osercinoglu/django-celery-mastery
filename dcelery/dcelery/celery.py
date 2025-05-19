import os
from celery import Celery
from kombu import Queue, Exchange
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE','dcelery.settings')
app = Celery("dcelery")
app.config_from_object("django.conf:settings", namespace='CELERY')

app.conf.task_queues = [
    Queue('tasks', Exchange('tasks'), routing_key='tasks',
    queue_arguments={
        'x-max-priority': 10,
    }),
]

app.conf.task_acks_late = True
app.conf.task_default_priority = 5
app.conf.worker_prefetch_multiplier = 1
app.conf.worker_concurrency = 1

@app.task(queue='tasks')
def t1(a, b, message=None):
    result = a + b
    if message:
        result = f"{message}: {result}"
    return result

@app.task(queue='tasks')
def t2():
    time.sleep(3)
    return

@app.task(queue='tasks')
def t3():
    time.sleep(3)
    return

def test():
    # Call the task asynchronously
    result = t1.apply_async(args=[4, 6], kwargs={"message":"The result is"})

    # Check if the task has completed
    if result.ready():
        print("Task completed")
        print(result.get())
    else:
        print("Task is still running")

    # Check if the task completed successfully
    if result.successful():
        print("Task was successful")
    else:
        print("Task failed")

    # Get the result of the task
    try:
        task_result = result.get(timeout=10)
        print("Task result:", task_result)
    except Exception as e:
        print("Error getting task result:", str(e))

    # Get the exception (if any) that occured during task execution
    exception = result.get(propagate=False)
    if exception:
        print("Task raised an exception:", str(exception))
    else:
        print("Task completed without exceptions")

#app.conf.task_routes = {
#    'newapp.tasks.*': {'queue': 'queue1'},
#    'newapp.tasks.task2': {'queue': 'queue2'},
#}

# app.conf.task_default_rate_limit = '1/m'

# app.conf.broker_transport_options = {
#     'priority_steps': (list(range(10))),
#     'sep':':',
#     'queue_order_strategy':'priority',
# }

app.autodiscover_tasks()