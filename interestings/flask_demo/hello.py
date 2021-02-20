from logging.config import dictConfig
import logging
from flask import Flask, escape, request, app

app = Flask(__name__)
# from flask.logging import default_handler
# app.logger.removeHandler(default_handler)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default',
    }},
    'loggers': {
        'yangkai': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    }
})
# root = logging.getLogger()
logger = logging.getLogger('yangkai')


# print(logger.parent.handlers)
# print(logger.parent)
# werkzeug_logger = logging.getLogger('werkzeug')
# werkzeug_logger.disabled = True
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    # 可以发现, 有2个logger, 一个是yangkai, 还有一个是werkzeug
    print(logging.root.manager.loggerDict)
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    print(loggers)
    logger.info('hello')
    return f'Hello, {escape(name)}!'


if __name__ == '__main__':
    # logger.warning('yangk')
    print(logging.root.manager.loggerDict)
    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    print(loggers)
