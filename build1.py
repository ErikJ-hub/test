import logging

# level=logging.INFO  (CRITICAL, ERROR, WARNING, INFO or DEBUG) #
logging.basicConfig(format='%(asctime)s - %(filename)s - %(levelname)s - %(message)s', level=logging.INFO)
# logging.setLevel(logging.INFO)
logger = logging.getLogger()

logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And this, too')
logger.critical('And this, too')

print(" - Enter: Build 1")

f = open("demo1.txt", "w")
f.writelines("1234567")
f.close()

f = open("demo2.txt", "w")
f.writelines("1234567")
f.close()

print(" - Exit:  Build 1")
