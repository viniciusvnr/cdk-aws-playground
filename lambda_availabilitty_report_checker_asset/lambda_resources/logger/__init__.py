import logging


class Logger:

    @classmethod
    def LogMsg(cls, msg, level='INFO'):
        cls.msg = msg
        cls.level = level
        cls._logger = logging.getLogger()

        if cls.level == 'ERROR':
            cls._logger.error(cls.msg)
        elif cls.level == 'WARN' or cls.level == 'WARNING':
            cls._logger.warning(cls.msg)
        elif cls.level == 'INFO':
            cls._logger.info(cls.msg)
        else:
            cls._logger.info('Logger level must be ERROR, WARNING or INFO')
