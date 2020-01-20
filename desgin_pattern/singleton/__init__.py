class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance


    def __init__(self, level):
        self.level = level

if __name__ == '__main__':
    logger1 = Logger('info')
    logger2 = Logger('debug')
    assert logger1 is logger2
    assert logger1.level == 'debug'
    assert logger2.level == 'debug'


