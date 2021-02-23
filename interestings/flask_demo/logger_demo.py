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
root2 = logging.getLogger('root')  # 这个不是root, 只有上一行才是root
ch = logging.StreamHandler()
root.addHandler(ch)
if __name__ == '__main__':
    logger = logging.getLogger('yangkai')
    logger2 = logging.getLogger('yangkai.foo')
    print(logger2.parent is logger)
    print(logger2.parent.parent is root)
    print(root is root2.parent)
    print(logger.parent.handlers)
    logger.info('yangk')
    logger2.info('yangkai2')
    print('loggers:', logging.root.manager.loggerDict)