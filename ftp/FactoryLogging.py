import logging
import threading

class factoryLogging(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(factoryLogging, "_instance"):
            with factoryLogging._instance_lock:
                if not hasattr(factoryLogging, "_instance"):
                    factoryLogging._instance = object.__new__(cls)
        return factoryLogging._instance

    def __init__(self):
        if( not hasattr(self,'logging') ):
            self.logging = self.__createLoggingObj()

    def __createLoggingObj(self):
        logger = logging.getLogger()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
        logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler('test.log', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        # 创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        logger.addHandler(fh)  # logger对象可以添加多个fh和ch对象
        logger.addHandler(ch)

        return logger

    def getLogging(self):
        return self.logging


if __name__ == '__main__':
    for i in range(10):
        logger = factoryLogging().getLogging()
        logger.info('logger debug message')
