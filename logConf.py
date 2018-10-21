import sys
import logging
from logging import handlers


def getLogger(name):
	logger = logging.getLogger(name)
	logger.setLevel(logging.INFO)

	logFormatter      = logging.Formatter('%(asctime)s  %(levelname)7s %(name)10s %(funcName)15s   %(message)s')

	logHandler        = logging.handlers.TimedRotatingFileHandler('logs/app', when="midnight")
	logHandler.suffix = "%Y%m%d%s"
	logHandler.setFormatter(logFormatter)

	ch = logging.StreamHandler(sys.stdout)
	ch.setFormatter(logFormatter)
	
	logger.addHandler(ch)
	logger.addHandler(logHandler)

	return logger






