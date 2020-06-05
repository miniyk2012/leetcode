# 读取日志配置文件内容
import logging.config

logging.config.fileConfig('logging.conf')

# 创建一个日志器logger
logger = logging.getLogger('simpleExample')
# 对于非root logger的level如果设置为NOTSET，系统将会查找高层次的logger来决定此logger的有效level

# 日志输出
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')