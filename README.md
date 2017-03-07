# django_rq_wrapper

Django management command for multiple rq workers in one command and autoreload.

---

This project builds off of [Django RQ](https://github.com/ui/django-rq). Instead of using the command `python manage.py rqworker high default low`, you can now run `python manage.py rqworkers high default low`.

### Installation

    pip install django-rq-wrapper

Add ``django_rq_wrapper`` to your installed apps. Use the management command ``rqworkers``.

### Added command options:

If you need to run multiple workers, you can pass in the ``--workers`` flag with the
number of workers you want to spawn. If you don't pass in this flag, the number of
workers will default to the environment variable ``RQ_CONCURRENCY``, or 1 if that
is not set::

    python manage.py rqworkers high default low --workers 5

If you would like to have your workers autoreload the same way django's runserver
autoreloads, use the ``--autoreload`` flag::

    python manage.py rqworkers high default low --autoreload

### Note for Heroku

Add the environment variable ``RQ_CONCURRENCY`` to your config with the number of workers
appropriate for (your dyno type)[https://devcenter.heroku.com/articles/optimizing-dyno-usage#python].
