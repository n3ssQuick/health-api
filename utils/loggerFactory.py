import logging


class LoggerLevels():
  LOG_LEVELS = {
      'DEBUG': logging.DEBUG,
      'INFO': logging.INFO,
      'WARNING': logging.WARNING,
      'ERROR': logging.ERROR,
      'CRITICAL': logging.CRITICAL
  }

  def getLoggerLevel(log_level):
    return LoggerLevels.LOG_LEVELS.get(log_level, logging.INFO)


class LoggerFactory():
  def getLogger(name: str = None, log_level: int = logging.INFO) -> logging.Logger:
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    # create formatter
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(name)s][%(filename)s:%(funcName)s:%(lineno)d] - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    return logger
