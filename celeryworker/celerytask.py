from celery import Celery

app = Celery('tasks')
app.config_from_object('celeryconfig')
app.conf.broker_transport_options = {
    'priority_steps': (list(range(10))),
    'sep':':',
    'queue_order_strategy':'priority',
}

app.autodiscover_tasks()