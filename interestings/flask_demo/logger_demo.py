import logging
import sys
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://sys.stdout',
        'formatter': 'default',
        'level': 'DEBUG'
    }},
    'loggers': {
        'yangkai': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    }
})
root = logging.getLogger()
ch = logging.StreamHandler()
root.addHandler(ch)
if __name__ == '__main__':
    logger = logging.getLogger('yangkai')
    print(logger.parent.handlers)
    logger.info('yangk')
    print('loggers:', logging.root.manager.loggerDict)